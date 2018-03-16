var alias = "";
var timer;
var chatText;

function saveAlias(){
	updateScroll();
	alias = this.document.getElementById("alias").value;
	this.document.getElementById("loginDiv").style.visibility = "hidden";
	this.document.getElementById("chatDiv").style.visibility = "visible";
	this.document.getElementById("aliasName").innerHTML = alias;
	timer = setInterval(function(){ getChatText() }, 500);
}

function setChatText(txt){
	this.document.getElementById("chatBoxDiv").innerHTML = txt;
	if(txt != chatText){
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
    xhttp.send(null);
}

function addMessage(){
		updateScroll();
		var msg = this.document.getElementById("msg").value;
		this.document.getElementById("msg").value = "";
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "addMessage.py", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send("message=<span class='aliasSpan'>"+alias+"</span>: "+msg);
}

function updateScroll(){
    var element = document.getElementById("chatBoxDiv");
    element.scrollTop = element.scrollHeight;
}

