from flask import jsonify
from window import WindowBase
import config


class WindowStockExchange(WindowBase):

    def __init__(self):
        super().__init__('stock_exchange')
