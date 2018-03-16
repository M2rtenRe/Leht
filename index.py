#!/usr/bin/python
import cgi

print("Content-type:text/html\r\n\r\n")

print('''
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Teretulemast</title>
    <link href="https://fonts.googleapis.com/css?family=Rubik+Mono+One" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Exo+2" rel="stylesheet">
    <link rel="icon" href="myspace.ico">
    <style>
      .submit{
        font-family: 'Exo 2', sans-serif;
        position: fixed;
        top: 50%;
        left: 50%;
        margin-top: -50px;
        margin-left: -25%;
        color: #ffffff;
        border: 0;
        height: 60px;
        width: 50%;
        background-color: #5a918b;
        -webkit-transition-duration: 0.4s;
        transition-duration: 0.4s;
        padding-left: 20px;
        padding-right: 20px;
        cursor: pointer;}

      .submit:hover {
        box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);}

      .submit1{
        font-family: 'Exo 2', sans-serif;
        position: fixed;
        top: 55%;
        left: 50%;
        margin-left: -25%;
        color: #ffffff;
        border: 0;
        height: 60px;
        width: 50%;
        background-color: #5a918b;
        -webkit-transition-duration: 0.4s;
        transition-duration: 0.4s;
        padding-left: 20px;
        padding-right: 20px;
        cursor: pointer;}

      .submit1:hover {
        box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);}
    </style>
  </head>
  <body style="display:flex; padding: 0;  width: 100%; overflow:hidden; align-items: center; justify-content: center; margin-top:10%; background-image:url(\'https://i.imgur.com/H3Crjxg.png\');">
    <h1 style="font-family: 'Rubik Mono One', sans-serif; font-size: 50px; color: white; -webkit-text-stroke: 0.5px #5a918b; ">Jututuba</h1>
    <form action="login.py" method="post">
    <input class="submit" type="submit" value="Sisse logimine"/>
    </form>
    <form action="register.py" method="post">
    <input class="submit1" type="submit" value="Registreerimine"/>
    </form>
  </body>
</html>
''')

