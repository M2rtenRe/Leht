#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi
import cgitb
import io
import re

TAG_RE = re.compile(r'<[^>]+>')
chatFile = io.open("/home/m2rtenreinaasoriginal/chat.txt", "r", encoding='utf-8')
result = ""

form = cgi.FieldStorage()
alias = form.getvalue("alias")

print("Content-type: text/html")
print("")
print("<head><meta charset='UTF-8'></head>")

if alias == "M2rtenRe":
	for row in chatFile.readlines():
		if row.split("-")[1].split(":")[0] == alias:
			result += '<span class="msgSpanRight" onclick="delMsg(this)"><p id="popup">'+row.split("-")[0]+'</p><span class="aliasSpan" id="msgName">'+row.split("-")[1].split(":")[0]+'</span>'
			result += ':'+row.split(":", 2)[2]+'</span><br>'
		else:
			result += '<span class="msgSpanLeft" onclick="delMsg(this)"><p id="popup">'+row.split("-")[0]+'</p><span class="aliasSpan" id="msgName">'+row.split("-")[1].split(":")[0]+'</span>'
			result += ':'+row.split(":", 2)[2]+'</span><br>'
else:
	for row in chatFile.readlines():
		if row.split("-")[1].split(":")[0] == alias:
			result += '<span class="msgSpanRight"><p id="popup">'+row.split("-")[0]+'</p><span class="aliasSpan">'+row.split("-")[1].split(":")[0]+'</span>'
			result += ':'+row.split(":", 2)[2]+'</span><br>'
		else:
			result += '<span class="msgSpanLeft"><p id="popup">'+row.split("-")[0]+'</p><span class="aliasSpan">'+row.split("-")[1].split(":")[0]+'</span>'
			result += ':'+row.split(":", 2)[2]+'</span><br>'

print(result)


