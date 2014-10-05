import os

from libcloud.compute.providers import get_driver as get_compute_driver
from libcloud.compute.types import Provider as ComputeProvider
from libcloud.compute.deployment import ScriptFileDeployment

from config import get_config
from oslogger import log


class Server(object):

    def __init__(self, config, deploy_name=None):
        self.config = config
        self.deploy_name = deploy_name
        self.compute = self.get_driver()

    def get_driver(self):
        # Get the compute driver we want to connect to, then pass in credentials.
        compute_driver = self.config["compute_driver"]
        ComputeDriver = get_compute_driver(compute_driver)

        identity = self.config["identity"]
        credential = self.config["credential"]
        rgn = self.config["region"]

        compute = ComputeDriver(identity, credential, region=rgn)
        log.info("Created a %s compute driver in the %s region.",
                 compute_driver, rgn)
        return compute

    def pair_ssh_key(self):
        # Pair our SSH public key with the provider so we can communicate
        # with our deployed compute nodes.

        public_key = self.config["public_key"]
        private_key = self.config["private_key"]
        
        pub_key = open(public_key, "r").read()

        key_name = os.path.split(private_key)[-1]
        keys = [key.name for key in self.compute.list_key_pairs()]
        
        if key_name not in keys:
            # If this key isn't already paired, import the key by choosing a name
            # and passing in the contents of the public key.
            key = self.compute.import_key_pair_from_string(key_name, pub_key)
            log.info("Paired %s key with provider.", key)
        else:
            log.info("Already had %s key paired.", key_name)

        return key_name

    def deployment_script(self):
        # Once the node is built, it'll be a bare image. Run the configured
        # bootstrap script using libcloud's ScriptDeployment to run the system
        # updates and install Flask.
        if self.deploy_name:
            deployment = ScriptFileDeployment(self.config[self.deploy_name])
            log.info("Created ScriptFileDeployment with %s file.", self.deploy_name)

        return deployment

    def create_node(self, name):
        """Create a compute node with a given name and configuration information.
        Return the Node object."""
        
        deployment = self.deployment_script()

        # Find the size and image we want to use when creating our node.
        # The following iterates through lists of sizes and images and finds
        # the match for our configured strings.
        size_name = self.config["size"]
        size = filter(lambda size: size.id == size_name, self.compute.list_sizes())[0]

        img_name = self.config["image"]
        image = filter(lambda image: image.name == img_name, self.compute.list_images())[0]

        log.info("Deploying node with size=%s, image=%s", size, image)

        # Deploy our node. This calls create_node but waits for the creation to
        # complete, and then it uses paramiko to SSH into the node and run
        # the commands specified by the `deploy` argument. In order to do this,
        # the paramiko SSH client must know the private key, specified in
        # `ssh_key`. `ex_keyname` is the public key we paired up above.
        key_name = self.pair_ssh_key()
        self.compute.region = self.config["region"]

        node = self.compute.deploy_node(name=name, image=image, size=size,
                    deploy=deployment,
                    ssh_key=self.config["private_key"],
                    ssh_username=self.config["ssh_user"],
                    ex_keyname=key_name,
                    ssh_timeout=6400,
                    timeout=6400)
        log.info("Node deployed: %s", node)

        return node
