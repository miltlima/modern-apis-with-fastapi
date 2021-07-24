# The hard way 

import datetime

from dateutil.parser import parse


order_json = {
    'item_id': '123',
    'created_date': '2019-01-01 12:34',
    'pages_visited': [1, 2, '3'],
    'price': 4.99
}

class Order:

    def __init__(self, item_id: int, created_date: datetime.datetime,
                pages_visited: None, price: float):
        if pages_visited is None:
            pages_visited = []
        
        try:
            self.item_id = int(item_id)
        except ValueError:
            raise Exception('item_id must be an integer')
        
        try:
            self.created_date = parse(created_date)
        except:
            raise Exception('created_date must be a valid date string')
        
        try:
            self.price = float(price)
        except ValueError:
            raise Exception('Invalid price, price must be a valid number')

        try:
            self.pages_visited = [int(p) for p in pages_visited]
        except:
            raise Exception('pages_visited must be a list of integers')

    def __str__(self):
        return f"item_id{self.item_id}, created_date{self.created_date}, pages_visited{self.pages_visited}, price{self.price}"

    def __eq__(self, other):
        return isinstance(other, Order) and self.__dict__ == other.__dict__
        
    def __ne__(self, other):
        return isinstance(other, Order) and self.__dict__ == other.__dict__


o = Order(**order_json)
print(o)
