import websocket
import threading
import json
from time import sleep

class APClient:
    def __init__(self, host, port, slot_name, grant_callback):
        self.host = host
        self.port = port
        self.slot = slot_name
        self.grant_callback = grant_callback
        self.ws = None

    def connect(self):
        url = f"ws://{self.host}:{self.port}/api"  
        self.ws = websocket.WebSocketApp(url,
                                         on_message=self.on_message,
                                         on_open=self.on_open)
        thread = threading.Thread(target=self.ws.run_forever, daemon=True)
        thread.start()

    def on_open(self, ws):
        print("Connected to AP server, authenticating...")
        auth = {'type': 'register', 'slot': self.slot}
        ws.send(json.dumps(auth))

    def on_message(self, ws, message):
        msg = json.loads(message)
        if msg.get('type') == 'received_item':
            item_name = msg['item_name']
            from_player = msg.get('from_player')
            self.grant_callback(item_name, from_player)
