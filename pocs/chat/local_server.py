'''
Starts a local websocket server on port 8765
'''
import os
import asyncio
import websockets
from dotenv import load_dotenv

load_dotenv(dotenv_path='pocs/chat/.chat.env')
socket_server_port = os.getenv('LOCAL_WEBSOCKET_SERVER_PORT')

async def handler(websocket):
    '''
    Handles the received messages and respond messages
    '''
    message = await websocket.recv()
    print(f'Server received:{message}')

    await websocket.send('Message received')
    print('Server responded')

async def main():
    '''Main function'''
    async with websockets.serve(handler,"localhost",socket_server_port):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
