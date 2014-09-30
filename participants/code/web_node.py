from nodes import Server

class WebServer(Server):
    def __init__(self, config):
        super(WebServer, self).__init__(config, "web_deployment")
