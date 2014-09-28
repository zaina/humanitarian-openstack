from nodes import Server

class DBServer(Server):
    def __init__(self, config):
        super(DBServer, self).__init__(config, "db_deployment")
