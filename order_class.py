from datetime import datetime
class Order:
    counter=0
    def __init__(self, items , date=None):
        self.items = items
        self.date = datetime.now()
order1 = Order(['meal-1', 'meal-2'])
print(order1.date)