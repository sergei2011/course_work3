import json
import operator
import datetime


def open_list(filename):
    """открываем файл с транзакциями"""
    with open(filename, 'r', encoding='utf-8') as file:
        transactions = json.load(file)
    return transactions

def sort_execut(trans):
    """перебираем список по выполненым транзакциям"""
    trans = [x for x in trans if "state" in x and x["state"] == "EXECUTED"]
    return trans


def sort_list(transactions):
    """сортируем по дате"""
    sort_trans = sorted(transactions, key=operator.itemgetter("date"), reverse=True)
    return sort_trans

def five_last(trans):
    """получаем последние пять операций"""
    last = trans[ :5 ]
    return last

def time(date):
    """преобразовываем дату"""
    date_time_obj = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return ( date_time_obj.strftime("%d.%m.%Y"))

def from_out(trans):
    if trans["from"]:
       sender = trans["form"]
    else:
        sender = []
    return sender



#q = open_list('../operations.json')
#w = sort_execut(q)
#e = sort_list(w)
#last_pay = five_last(e)
#t = last_pay[1]['date']
#time(t)