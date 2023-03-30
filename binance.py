# pip install websocket-client
import websocket
import threading
import time
import json


first_price = float(0)

class SocketConn(websocket.WebSocketApp):
    def __init__(self, url):
        # WebSocketApp sets on_open=None, pass socketConn.on_open to init
        super().__init__(url=url, on_open=self.on_open)

        # self.params = params
        self.on_message = lambda ws, msg: self.message(msg)

        self.on_error = lambda ws, e: print('Error', e)
        self.on_close = lambda ws: print('Closing')

        self.run_forever()

    def on_open(self, ws,):
        print('Websocket was opened')

    def message(self, msg):
        global first_price
        test = json.loads(msg)

        new_price = float(test['k']['c'])

        if first_price == 0.0:
            first_price = new_price
            print('first_price = ', first_price)

        delta = first_price - new_price
        print(f'first price = {first_price} | new_price = {new_price} | delta = {round(delta,6):0.6f}')


threading.Thread(target=SocketConn, args=('wss://stream.binance.com:443/ws/ethbtc@kline_1m',)).start()



