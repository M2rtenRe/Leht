#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi,sys,io,re
import datetime

currentDate = datetime.datetime.now() + datetime.timedelta(hours=2)
currentDate = currentDate.strftime("%m/%d %H:%M")

TAG_RE = re.compile(r'<[^>]+>')
result = ""
params = cgi.FieldStorage()
message = params.getvalue("message")

print("Content-type: text/html; charset='UTF-8'\r\n\r\n")

with io.open("/home/m2rtenreinaasoriginal/banned.txt", "r", encoding='utf-8') as f:
    for name in f.readlines():
        if name.strip() == message.split(":")[0]:
            sys.exit()

if message.split(":", 1)[1] == " ":
    sys.exit()

with io.open("/home/m2rtenreinaasoriginal/ropud.txt", "r", encoding='utf-8') as f:
    wordFilter = f.readlines()
    wordFilter = [x.strip() for x in wordFilter]
    for word in map(lambda x:x.lower(),message.split()):
        for badword in wordFilter:
            if badword in word:
                sys.exit()

with io.open("/home/m2rtenreinaasoriginal/chat.txt", "a", encoding='utf-8') as chatFile:
    result += currentDate+'-'
    result += TAG_RE.sub('', message.split(":")[0])
    result += ":" + TAG_RE.sub('', message.split(":", 1)[1])
    chatFile.write(result+"\n")

print(message)
