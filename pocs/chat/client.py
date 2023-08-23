'''
Simple call test to apigateway websocket POC api.
'''
import os
import json
import asyncio
import websockets
from dotenv import load_dotenv

load_dotenv(dotenv_path='pocs/chat/.chat.env')

server_socket_url = os.getenv('WEB_SOCKET_CLIENT2SERVER_URL')
local_socket_server_port = os.getenv('LOCAL_WEBSOCKET_SERVER_PORT')
local_uri=f'ws://localhost:{local_socket_server_port}'

async def connect():
    '''Stablish the connection with api gateway'''

    mode = input('local or remote[l/r]:')
    uri = local_uri if mode == 'l' else server_socket_url
    
    async with websockets.connect(uri) as websocket:
        message = input('Insert a message:')
        json_message={
            'action':'send_message',
            'message':message
        }
        await websocket.send(json.dumps(json_message))
        print(f'Client sent:{message}')

        answer = await websocket.recv()
        print(f'Server responds with:{answer}')

if __name__ == "__main__":
    asyncio.run(connect())
