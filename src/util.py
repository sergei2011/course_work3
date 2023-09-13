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
    """выод исходящего счета со скрытыми цифрами"""
    if "from" in trans:
        if trans['from'][0] == 'С':
            sender = trans['from'][:-20] + '**** **** **** **** ' + trans['from'][-4:]
        else:
            sender = trans['from'][:-12] + ' ' + trans['from'][-12:-10] + '** **** ' + trans['from'][-4:]
    else:
        sender = ''
    return sender

def to_in(trans):
    """вывод принимающего счета со скрытыми цифрами"""
    if trans['to'][0] == 'С':
        receiver = trans['to'][:-20] + '**** **** **** **** ' + trans['to'][-4:]
    else:
        receiver = trans['to'][:-12] + ' ' + trans['to'][-12:-10] + '** **** ' + trans['to'][-4:]

    return receiver

