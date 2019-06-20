#!/usr/bin/env bash

~/julius/julius-4.5/julius/julius -C ~/julius/julius-kit/dictation-kit-4.5/main.jconf -C ~/julius/julius-kit/dictation-kit-4.5/am-gmm.jconf -nostrip -module > /dev/null &
echo $! #プロセスIDを出力
sleep 2 #2秒間スリープ
