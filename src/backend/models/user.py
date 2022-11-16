from node import Node

class User(Node):
    def __init__(self, ip, port) -> None:
        super().__init__(ip, port)
    