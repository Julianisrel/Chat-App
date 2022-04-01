class Person:
    """
    Represents a person, holds name, socket client and IP address
    """
    def __init__(self, addr, client):
        self.addr = addr
        self.client = client
        self.name = None
