# -*- coding: utf-8 -*-
import requests
import shelve
import socket
import time

host = 'localhost'
port = 10500

# base ----------
def use_shelf(key):
    shelf = shelve.open(bot_shelf)
    val = shelf[key]
    shelf.close()
    return val


def run_julius():
    try:
        subprocess('run_juliuscmd')
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
    except Exception as e:
        print('Juliusの起動に失敗しました :' + e)


def kill_julius():
    try:
        subprocess('kill_juliuscmd')
    except Exception as e:
        print('Juliusの終了に失敗しました :' + e)


def julius():
    run_julius()
    try:
        res = ''
        while (res.find('\n.') == -1):
            res += sock.recv(1024)
        word = ''
        for line in res.split('\n'):
            index = line.find('WORD=')
            if index != -1:
                line = line[index + 6:
                    line.find('"', index + 6)]
                if line != '[s]':
                    word = word + line
    except Exception as e:
        print('音声分析に失敗しました :' + e)
    res = ''
    kill_julius()
    return word


def jtalk():
    ```Open JTalk
    ```


# add -----------
def weather_forecast(location):
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
    payload = {'city':'130010'}
    data = requests.get(url, params=payload).json()
    where = data['title']
    telop = data['forecasts'][1]['telop'])
    max_temperature = data['forecasts'][1]['temperature']['max']['celsius'])
    result = [where, telop, max_temperature]
    return result


if __name__: '__main__':
    while True:
        word = julius()
        if word == 'こんにちは':
            jtalk('こんにちは！')
        elif word == '名前覚えて'
            jtalk('おっけー。今は%sって呼んでるよ' % (use_shelf('username')))
            use_shelf('username') = julius()
            jtalk('%sだね。覚えたよ' % (use_shelf('username')))
        elif word == '住所覚えて':
            jtalk('どこ住み？')
            use_shelf('address') = julius()
            jtalk(use_shelf('address') + 'だね。覚えたよ')
        elif word == '勤務先覚えて':
            jtalk('職場どこ？')
            use_shelf('work_address') = julius()
            jtalk(use_shelf('work_address') + 'だね。覚えたよ')
        elif word == '明日の天気教えて':
            jtalk('どこの？')
            type = julius()
            result
            if type == '住所':
                result = weather_forecast(use_shelf('address'))
            elif type == '勤務先':
                result = weather_forecast(use_shelf('work_address'))
            jtalk('明日の%sは%sだよ。最高気温は%s！' % (result[0], result[1], result[3]))
        elif word == 'c':
            jtalk('またね')
            use_shelf.close
            subprocess('ctrl+c')
        else:
            jtalk(word)

# https://www.sejuku.net/blog/23044
# https://www.pc-koubou.jp/magazine/20637
