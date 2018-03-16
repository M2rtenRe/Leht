#!/usr/bin/python
import cgi,io

print("Content-type:text/html\r\n\r\n")

form = cgi.FieldStorage()
deletedMsg = form.getvalue("deletedMsg")
deletedMsgFinal = ""
deletedMsgFinal += deletedMsg.split('<p id="popup">')[1].split("</p>")[0]
deletedMsgFinal += "-"
deletedMsgFinal += deletedMsg.split('id="msgName">')[1].split("</span>")[0]
deletedMsgFinal += deletedMsg.split("</span>")[1]

f = io.open("/home/m2rtenreinaasoriginal/chat.txt", "r", encoding='utf-8')
lines = f.readlines()
f.close()

f = io.open("/home/m2rtenreinaasoriginal/chat.txt", "w", encoding='utf-8')
for line in lines:
    if line != deletedMsgFinal:
        f.write(line)
f.close()

