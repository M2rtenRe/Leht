#!/usr/bin/python
import hashlib,sys,getpass,base64,os,random,string,urllib.request,subprocess,socket,rngCam,time,cgi

loginCount = 0
userCount = 0
print("Content-type:text/html\r\n\r\n")
print('''<!DOCTYPE html>
<html>
<head><title>Sisselogimine</title><link rel="icon" href="myspace.ico"><meta name="viewport" content="width=device-width, initial-scale=1"><link href="https://fonts.googleapis.com/css?family=Krona+One" rel="stylesheet"><link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet">
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
<body style="display:flex; padding: 0; width: 100%; overflow:hidden; align-items: center; justify-content: center; margin-top: 10%; background-image:url(\'Tzs62qH.png\');">''')

def checkUser(passwordIn):
    global userIn
    f = open("/home/m2rtenreinaasoriginal/kasutajad.txt", "r")
    passListDecode = f.read()
    passList = passListDecode.splitlines()
    if userIn == None:
        userIn = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation) for n in range(10)).replace("-", "").replace(",","").replace(":","")
    for line in passList:
        if line.split(":")[0].strip().lower() == userIn.lower():
            userIn = line.split(":")[0].strip()
            f.close()
            return checkPass(passwordIn)
    return False
    f.close()

def checkPass(passwordIn):
    f = open("/home/m2rtenreinaasoriginal/kasutajad.txt", "r")
    passListDecode = f.read()
    passList = passListDecode.splitlines()
    if passwordIn == None:
        passwordIn = "a"
    for line in passList:
        pp = ""
        pp += line.split("-")[1].split(",")[0].strip()
        pp += passwordIn
        passInHash = hashlib.sha512(pp.strip().encode()).hexdigest()
        if line.split(":")[1].strip().split("-")[0].strip() == passInHash:
            f.close()
            return True

    return False
    f.close()

form = cgi.FieldStorage()
if form.getvalue("back") != None:
    print("<p>Tagasi minek...</p>")
    print('<meta http-equiv="refresh" content="0; url=index.py"/>')
    sys.exit()
if form.getvalue("Sisesta") != None:
    userIn = form.getvalue("username")
    passwordIn = form.getvalue("password")
    userCheck = checkUser(passwordIn)
    if userCheck == False:
        print('<p style="font-family: \'Montserrat\', sans-serif; position: absolute; margin-top: -200px; color: #ffffff;">ERROR: Vale kasutajanimi voi parool!</p>')
    if userCheck == True:
        print("""
        <head>
        	<link rel="stylesheet" type="text/css" href="style.css">
            <meta name="viewport" content="width=device-width, initial-scale=1" />
            <link href="https://fonts.googleapis.com/css?family=Arimo|Marmelad" rel="stylesheet">
            <script>
                document.title = "Jututuba"
        		var alias = \""""+userIn+"""\";
        		var timer;
        		var chatText;
                var audio = new Audio('MSN.wav');
                var w = window,
                    d = document,
                    e = d.documentElement,
                    g = d.getElementsByTagName('body')[0],
                    x = w.innerWidth || e.clientWidth || g.clientWidth;
                document.body.style.background = "url(\'https://i.imgur.com/j8IEfV4.gif\')";
                document.body.style.backgroundPositionY = "-5vw";
                if (x < 720){
                    document.body.style.backgroundPosition = "80\% 70\%";
                }

                function muteUser(command,mutedname){
                    var xhttp = new XMLHttpRequest();
                    xhttp.open("POST", "muteUser.py", true);
        		    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        		    xhttp.send("alias="+mutedName+"&command="+command);
                }

                function delMsg(deletedMsg){
                    var xhttp = new XMLHttpRequest();
                    deletedMsg = deletedMsg.innerHTML;
                    xhttp.open("POST", "deleteMsg.py", true);
        		    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        		    xhttp.send("deletedMsg="+deletedMsg);
                }

        		function saveAlias(){
        			updateScroll();
        			this.document.getElementById("chatDiv").style.visibility = "visible";
                    this.document.getElementById("aliasName").innerHTML = alias;
        			timer = setInterval(function(){ getChatText() }, 500);
        		}

        		function setChatText(txt){
        			this.document.getElementById("chatBoxDiv").innerHTML = txt;
        			if(txt != chatText){
                        audio.play();
                        updateScroll();
        			}
        			chatText = txt;
        		}

        		function getChatText(){
        		    var xhttp = new XMLHttpRequest();
        		    xhttp.onreadystatechange = function() {
        		        if (this.readyState == 4 && this.status == 200) {
        		            setChatText(this.response);
        		        }
        		    };
        		    xhttp.open("POST", "getChat.py", true);
        		    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        		    xhttp.send("alias="+alias);
        		}

        		function addMessage(){
        			updateScroll();
        			var msg = this.document.getElementById("msg").value;
        			this.document.getElementById("msg").value = "";
                    if (alias == "M2rtenRe"){
                        if (msg.substring(0,5) == "/mute"){
                            mutedName = msg.substring(6);
                            muteUser("mute",mutedName);
                        }
                        else if(msg.substring(0,7) == "/unmute"){
                            mutedName = msg.substring(8);
                            muteUser("unmute",mutedName);
                        }
                        else{
                		    var xhttp = new XMLHttpRequest();
                            console.log(msg);
                		    xhttp.open(\"POST\", \"addMessage.py\", true);
                		    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                		    xhttp.send("message="+alias+": "+msg);
                        }
                    }
                    else{
                        var xhttp = new XMLHttpRequest();
                        xhttp.open(\"POST\", \"addMessage.py\", true);
                        xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                        xhttp.send("message="+alias+": "+msg);
                    }
                }

        		function updateScroll(){
        		    var element = document.getElementById("chatBoxDiv");
        		    element.scrollTop = element.scrollHeight;
        		}

                function enterKeyPress(){
                    if (event.keyCode === 13) {
                        document.getElementById("send").click();}
                }
        	</script>
        </head>
        <body onLoad="saveAlias()">
        	<div id="chatDiv" style="visibility: hidden">
        		<h3 style="font-family: 'Marmelad', sans-serif; font-size: 30px; color: #ffffff; text-shadow: 2px 2px 4px #000000;">Teretulemast <span id="aliasName"/></h3>
        		<div class="outer"><div id="chatBoxDiv" class="chatBox">
                </div>
        		</div>
                <div class="messageArea">
        		<input type="textarea" id="msg" onkeypress="enterKeyPress()">
        		<button id="send" onclick="addMessage()">Saada</button>
                </div>
        	</div>
        </body>
        """)
        sys.exit()

print('<form action="login.py" method="post">')
print('''
<h1 style="font-family: \'Krona One\', sans-serif; font-size: 50px; color: #ffffff; -webkit-text-stroke: 0.5px #409e5f;">Sisse logimine</h1>
<p style="font-family: \'Montserrat\', sans-serif; margin-left: 10%; color: #ffffff;">Kasutajanimi: </p><input style="border: 2px solid #409e5f; height: 25px; width: 80%; margin-left: 10%; min-width: 40%; "type="text" name="username"/>
<p style="font-family: \'Montserrat\', sans-serif; margin-left: 10%; color: #ffffff;">Parool: </p><input style="border: 2px solid #409e5f; height: 25px; width: 80%; margin-left: 10%; min-width: 40%;" type="password" name="password"/><br />
<input class="submit" type="submit" value="Logi sisse" name="Sisesta"/>
<input class="submit1" type="submit" value="Tagasi" name="back"/>
</form>''')
print("</form>")
print('</body>')
print('</html>')
