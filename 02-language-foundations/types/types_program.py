from collections import namedtuple
from typing import Iterable
from typing import Optional

Item = namedtuple('Item', 'name, value')


running_max: Optional[int] = None

def counter(items: Iterable[Item]) -> int:
    global running_max
    
    total = 0

    for i in items:
        total += i.value

    if not running_max or total > running_max:
        running_max = total
    
    return total

def main():
    print("Let's create some items")

    dinner_items = [Item('Pizza',20), Item('Cake',5), Item('Cookie',1)]
    breakfast_items = [Item('Eggs',50), Item('Bacon',10), Item('Toast',1)]

    dinner_total = counter(dinner_items)
    print(f"Dinner was ${dinner_total:,.02f}")

    breakfast_total = counter(breakfast_items)
    print(f"Breakfast was ${breakfast_total:,.02f}")

    print(f"Today your most expensive meal costs ${running_max:,.02f}")

main()