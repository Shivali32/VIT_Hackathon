
function pr() {
    var data = document.getElementById('userBox').value;
    var user = document.getElementById("userBox").value;
    document.getElementById("userBox").value = "";
    document.getElementById("chatLog").innerHTML += "<b>You </b>" + "<span>" + user + "</span>" +"<br>";
    
    var settings = {
      "url": "https://bloomindia.herokuapp.com/chatbotapi/",
      "method": "POST",
      "timeout": 0,
      "headers": {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      "data": {
        "user_message": data
      }
    };
    
    $.ajax(settings).done(function (response) {
      document.getElementById("chatLog").innerHTML += "<b>Chatbot </b>" + "<div class=\"bot-message\">" + response.bot_message + "<\/div>" + "<br>";
    });
    }
  


function openChatbot() {
  document.getElementById("chatbutton").style.display = "none";
	document.getElementById("chatwindow").style.display = "block";
}

function closeChatbot() {
	
  	document.getElementById("chatwindow").style.display = "none";
	document.getElementById("chatbutton").style.display = "block";
} 
