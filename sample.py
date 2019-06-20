# -*- coding: utf-8 -*-
import socket
import subprocess
import time

host = 'localhost'
port = 10500

def pull_shelf(key, val):
    shelf = shelve.open(bot_shelf)
    shelf[key] = val
    shelf.close()

def get_shelf(key):
    shelf = shelve.open(bot_shelf)
    val = shelf[key]
    shelf.close()
    return val

def jtalk(t):
    """Open JTalkによる音声生成, 出力.
    """
    open_jtalk=['open_jtalk']
    mech=['-x','/var/lib/mecab/dic/open-jtalk/naist-jdic']
    htsvoice=['-m','/usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice']
    speed=['-r','1.0']
    outwav=['-ow','open_jtalk.wav']
    cmd=open_jtalk+mech+htsvoice+speed+outwav
    c = subprocess.Popen(cmd,stdin=subprocess.PIPE)
    c.stdin.write(t)
    c.stdin.close()
    c.wait()
    aplay = ['aplay','-q','open_jtalk.wav']
    wr = subprocess.Popen(aplay)

def listen_by_julius():
	# cmd='~/julius/julius-4.5/julius/julius -C ~/julius/julius-kit/dictation-kit-4.5/main.jconf -C ~/julius/julius-kit/dictation-kit-4.5/am-gmm.jconf -nostrip -module'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    res = 	''
    while True:
        while (res.find('\n.') == -1):
            res += sock.recv(1024)
        word = ''
        for line in res.split('\n'):
            index = line.find('WORD=')
            if index != -1:
                line = line[index + 6 : line.find('"', index + 6)]
                if line != '[s]':
                    word = word + line
            if word == 'テスト':
                print('!!!!!!!!!!!')
            print(word)
            jtalk('きこえたよ')
            res = ''

if __name__ == '__main__':
    while True:
        print('入力してください')
        jtalk('入力してください')
        word = input()
        print(word)
        if word == 'こんにちは':
            jtalk('こんにちは！')
        elif word == '名前覚えて':
            # jtalk('おっけー。今は%sって呼んでるよ' % (use_shelf('username')))
            put_shelf('username', input())
            jtalk('%sだね。覚えたよ' % (use_shelf('username')))
        elif word == '住所覚えて':
            jtalk('どこ住み？')
            put_shelf('address', input())
            jtalk(use_shelf('address') + 'だね。覚えたよ')
        elif word == '勤務先覚えて':
            jtalk('職場どこ？')
            put_shelf('work_address', input())
            jtalk(use_shelf('work_address') + 'だね。覚えたよ')
        elif word == '明日の天気教えて':
            jtalk('どこの？')
            type = julius()
            result
            if type == '住所':
                result = weather_forecast(get_shelf('address'))
            elif type == '勤務先':
                result = weather_forecast(get_shelf('work_address'))
            jtalk('明日の%sは%sだよ。最高気温は%s！' % (result[0], result[1], result[3]))
        elif word == 'c':
            jtalk('またね')
            #subprocess('ctrl+c')
        else:
            jtalk(word)
        word = ''
