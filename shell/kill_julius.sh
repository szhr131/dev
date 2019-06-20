#!/usr/bin/env bash

ps ax | grep julius | grep -v grep | awk '{print $1}' | xargs kill
