from config import get_config
from oslogger import log
from nodes import Server

if __name__ == "__main__":
    config = get_config()

    log.info("Creating web nodes.")
    nodes = []
    for name in ("mcw-1", "mcw-2"):
        server = Server(name, config, deploy_name="web_deployment")
        nodes.append(server.create_node())
