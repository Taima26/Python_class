from datetime import datetime
from functions import cal_counter, price_counter
class Order:
    counter=0
    def __init__(self, items , date=None):
        self.items = items
        self.date = datetime.now()
        self.order_id = f"order-{Order.counter}"
        Order.counter +=1
        self.order_accepted = bool
        self.order_refuse_reason = str
   
    def is_order_accepted(self):
        if cal_counter(self.items) is int:
            self.order_accepted = True
            self.order_refuse_reason = None
        elif cal_counter(self.item) == "Wrong input":
            self.order_accepted = False
            self.order_refuse_reason = "Wrong input"
        elif cal_counter(self.items) > 2000:
            self.order_accepted = False
            self.order_refuse_reason = "meal too big"
        
order1 = Order(['meal-1', 'meal-2'])
