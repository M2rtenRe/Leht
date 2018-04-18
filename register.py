#!/usr/bin/python
import hashlib,sys,getpass,base64,os,random,urllib.request,subprocess,socket,rngCam,time,cgi,sqlite3

conn = sqlite3.connect('/home/m2rtenreinaasoriginal/Kasutajad.db')

c = conn.cursor()
with conn:
    c.execute("SELECT * FROM kasutajad")

print("Content-type:text/html\r\n\r\n")

print('''<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Registreerimine</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://fonts.googleapis.com/css?family=Krona+One" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet">
  <link rel="icon" href="myspace.ico">
  <style>
  .submit{
    margin-top: 5%;
    margin-left: 10%;
    height: 40px;
    width: 40%;
    border: 2px solid #409e5f;
    color: #000000;
    background-color: #ffffff;
    -webkit-transition-duration: 0.4s;
    transition-duration: 0.4s;
    padding-left: 20px;
    padding-right: 20px;
    border-radius: 8px;
    cursor: pointer;}

    .submit:hover {
    background-color: #409e5f;
    color: white;}

    .submit1{
      height: 40px;
      width: 40%;
      border: 2px solid #409e5f;
      color: #000000;
      background-color: #ffffff;
      -webkit-transition-duration: 0.4s;
      transition-duration: 0.4s;
      padding-left: 20px;
      padding-right: 20px;
      border-radius: 8px;
      cursor: pointer;}

    .submit1:hover {
      background-color: #409e5f;
      color: white;}
</style>
</head>
<body style="display:flex; padding: 0; width: 100%; overflow:hidden; align-items: center; justify-content: center; margin-top:10%; background-image:url(\'https://i.imgur.com/Tzs62qH.png\');">''')

def createUser(newname,newpass):
    with open("/home/m2rtenreinaasoriginal/ipBanned.txt", "r") as f:
        for line in f.readlines():
            if cgi.escape(os.environ["HTTP_X_FORWARDED_FOR"]).strip() == line.strip():
                return "Banned"
    if newname == None:
        return "Kasutajanimi"
    elif newpass == None:
        return "Parool"
    for line in c.fetchall():
        if newname.lower() == line[0].lower():
            return "Kasutusel"
    saltPass = rngCam.captureCam(0)
    if saltPass == "No connection":
        return "Uhendus"
    newPasss = ""
    newPasss += saltPass
    newPasss += newpass
    newPassHash = hashlib.sha512(newPasss.strip().encode()).hexdigest()
    with conn: c.execute("INSERT INTO kasutajad VALUES (?, ?, ?, ?, ?)", newname, newPassHash, saltPass, cgi.escape(os.environ["HTTP_X_FORWARDED_FOR"]), "NO")
    return "Tehtud"

form = cgi.FieldStorage()
if form.getvalue("back") != None:
    print("<p>Tagasi minek...</p>")
    print('<meta http-equiv="refresh" content="0; url=index.py"/>')
    sys.exit()
if form.getvalue("Sisesta") != None:
    newName = form.getvalue("username")
    newPass = form.getvalue("password")
    newUserCheck = createUser(newName,newPass)
    if newUserCheck == "Banned":
        print('<p style="font-family: \'Montserrat\', sans-serif; position: absolute; margin-top: -200px; color: #ffffff;">ERROR: IP on keelatud!</p>')
    if newUserCheck == "Uhendus":
        print('<p style="font-family: \'Montserrat\', sans-serif; position: absolute; margin-top: -200px; color: #ffffff;">ERROR: Ei suutnud serveriga uhendust luua!</p>')
    if newUserCheck == "Kasutajanimi":
        print('<p style="font-family: \'Montserrat\', sans-serif; position: absolute; margin-top: -200px; color: #ffffff;">ERROR: Kasutajanimi peab olema vahemalt 1 taht!</p>')
    if newUserCheck == "Parool":
        print('<p style="font-family: \'Montserrat\', sans-serif; position: absolute; margin-top: -200px; color: #ffffff;">ERROR: Parool peab olema vahemalt 1 taht!</p>')
    if newUserCheck == "Kasutusel":
        print('<p style="font-family: \'Montserrat\', sans-serif; position: absolute; margin-top: -200px; color: #ffffff;">ERROR: Kasutajanimi juba kasutusel!</p>')
    if newUserCheck == "Tehtud":
        print('<meta http-equiv="refresh" content="0; url=login.py"/>')

print('<form action="register.py" method="post">')
print('''<h1 style="font-family: 'Krona One', sans-serif; font-size: 50px; color: #ffffff; -webkit-text-stroke: 0.5px #409e5f;">Kasutaja tegemine</h1>
<p style="font-family: 'Montserrat', sans-serif; margin-left: 10%; color: #ffffff;">Uus kasutajanimi: </p><input style="border: 2px solid #409e5f; height: 25px; width: 80%; margin-left: 10%; "type="text" name="username"/>
<p style="font-family: 'Montserrat', sans-serif; margin-left: 10%; color: #ffffff;">Uus parool: </p><input style="border: 2px solid #409e5f; height: 25px; width: 80%; margin-left: 10%; " type="password" name="password"/><br />
<input class="submit" type="submit" value="Registreeri" name="Sisesta"/>
<input class="submit1" type="submit" value="Tagasi" name="back"/>
</form>''')

print('</body>')
print('</html>')
