from nodes import Server
from libcloud.compute.deployment import ScriptDeployment

class HAProxyServer(Server):
    def __init__(self, config, nodes):
        self.nodes = nodes
        super(HAProxyServer, self).__init__(config, "haproxy")

    def prepare_haproxy_config(self, path, nodes):
        """Open the haproxy template and add the created nodes."""
        lines = open(path, "r").readlines()

        # Append the web server node private (internal) IPs to the config.
        for node in self.nodes:
            lines.append("        server %s %s\n" % (node.name,
                                                     node.private_ips[0]))
        return "".join(lines)

    def deployment_script(self):
        haproxy_config = self.prepare_haproxy_config(self.config["haproxy"], self.nodes)
        # Insert the haproxy.cfg file into the deployment script.
        haproxy_deploy = open(self.config["haproxy_deploy"], "r").read()
        script = haproxy_deploy % ({"config" : haproxy_config})
        deployment = ScriptDeployment(script.encode("utf8"))

        return deployment
