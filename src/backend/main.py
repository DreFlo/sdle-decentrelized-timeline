import sys
import asyncio
from kademlia.network import Server

from communication import sender
from communication import listener
'''
python main.py -register 'name' 'port'
python main.py -timeline 'name'

'''

async def main():
    #server = Server()
    
    #boostrap_node = (sys.argv[1], int(sys.argv[2]))
    #await server.bootstrap([boostrap_node])
    if(len(sys.argv) == 4): # ip port msg
        await sender.send_message(sys.argv[1], int(sys.argv[2]), sys.argv[3]), asyncio.get_event_loop()
    else: #ip port
        #await server.listen(int(sys.argv[2]))
        server_listener = listener.Listener(sys.argv[1], int(sys.argv[2]))
        server_listener.daemon = True

        server_listener.start()

        try:
            while True:
                pass
        except KeyboardInterrupt:
            server_listener.stop()
        
    #server.stop()
    
    #node = Node(sys.argv[1], int(sys.argv[2]), sys.argv[3])

if __name__ == "__main__":
    asyncio.run(main())