# This is a sample Python script.
from src.util import open_list, sort_execut, sort_list, five_last, time, from_out, to_in

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

q = open_list('../operations.json')
w = sort_execut(q)
e = sort_list(w)
last_pay = five_last(e)

for x in last_pay:
   time_pay = time(x['date'])
   sender = from_out(x)
   receiver = to_in(x)
   print(f"{time_pay}  {x['description']} \n{sender} -> {receiver}\n{x['operationAmount']['amount']} {x['operationAmount']['currency']['name']}\n")

