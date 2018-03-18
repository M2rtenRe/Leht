#!/usr/bin/python
import cgi

form = cgi.FieldStorage()
user = form.getvalue("alias")
command = form.getvalue("command")

print("Content-type:text/html\r\n\r\n")

if command == "ban":
    with open("/home/m2rtenreinaasoriginal/kasutajad.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.split(":")[0].strip() == user:
                ip = line.split(",")[1]
                with open("/home/m2rtenreinaasoriginal/ipBanned.txt", "a") as ff:
                    ff.write(ip)

    f = open("/home/m2rtenreinaasoriginal/kasutajad.txt", "r")
    lines = f.readlines()
    f.close()

    with open("/home/m2rtenreinaasoriginal/kasutajad.txt", "r") as f:
        linos = f.readlines()
        for line in linos:
            if line.split(":")[0].strip() == user:
                banLine = line

    try:
        if banLine != None:
            f = open("/home/m2rtenreinaasoriginal/kasutajad.txt", "w")
            for line in lines:
                if line == banLine:
                    f.write("#"+banLine)
                if line != banLine:
                    f.write(line)
            f.close()
    except NameError:
        pass

if command == "unban":
    with open("/home/m2rtenreinaasoriginal/kasutajad.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.split(":")[0].strip() == user:
                ip = line.split(",")[1]
                f = open("/home/m2rtenreinaasoriginal/ipBanned.txt", "r")
                lines = f.readlines()
                f.close()
                with open("/home/m2rtenreinaasoriginal/ipBanned.txt", "w") as ff:
                    for line in lines:
                        if line != ip:
                            ff.write(line)

    f = open("/home/m2rtenreinaasoriginal/kasutajad.txt", "r")
    lines = f.readlines()
    f.close()

    with open("/home/m2rtenreinaasoriginal/kasutajad.txt", "r") as f:
        linos = f.readlines()
        for line in linos:
            if line.split(":")[0].strip() == "#"+user:
                banLine = line
    try:
        if banLine != None:
            f = open("/home/m2rtenreinaasoriginal/kasutajad.txt", "w")
            for line in lines:
                if line.split(":")[0].strip() == banLine.split(":")[0].strip():
                    f.write(line.replace("#", "", 1))
                if line != banLine:
                    f.write(line)
            f.close()
    except NameError:
        pass
