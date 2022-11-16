import logging
import asyncio
import sys

from kademlia.network import Server

# python get.py <bootstrap node> <bootstrap port> <key>
# get.py 1.2.348 3244 SpecialKey


class Node:
    def __init__(self, ip : str, port : int, name : str) -> None:
        self.setup_logger()

        self.ip = ip
        self.port = port
        self.name = name

        self.server = Server()
        
        asyncio.run(self.testListen())

    def setup_logger(self):
        logging.basicConfig(level=logging.DEBUG)
        logging.getLogger("kademlia").setLevel(logging.INFO)

    async def testListen(self):
        if(self.name != "hello"):
            self.name = "hello"
        
        await self.server.listen(self.port)
        
        bootstrap_node = (self.ip, self.port)
        await self.server.bootstrap([bootstrap_node])
        #await self.server.set(self.name, "Hello World")
        
        result = None
        stay = True
        result = await self.server.get(self.name)
        #result = await self.server.get(self.name)
        print("Result: {}".format(result))
        self.server.stop()


def main():
    node = Node(sys.argv[1], int(sys.argv[2]), sys.argv[3])


if __name__ == "__main__":
    main()