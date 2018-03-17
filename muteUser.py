#!/usr/bin/python
import cgi,io

form = cgi.FieldStorage()
alias = form.getvalue("alias")
command = form.getvalue("command")

print("Content-type:text/html\r\n\r\n")
print("<html><head><meta charset='UTF-8'></head>")

if command == "mute":
    with io.open("/home/m2rtenreinaasoriginal/banned.txt", "r", encoding='utf-8') as f:
        for line in f.readlines():
            if line == "alias":
                sys.exit()
    with io.open("/home/m2rtenreinaasoriginal/banned.txt", "a", encoding='utf-8') as f:
        f.write(alias+"\n")

if command == "unmute":
    f = io.open("/home/m2rtenreinaasoriginal/banned.txt", "r", encoding='utf-8')
    lines = f.readlines()
    f.close()

    f = io.open("/home/m2rtenreinaasoriginal/banned.txt", "w", encoding='utf-8')
    for line in lines:
        if line != alias:
            f.write(line)
    f.close()
