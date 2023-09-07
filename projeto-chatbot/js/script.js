const messageInput = document.getElementById("message-input").value.trim();
const sendButton = document.getElementById("send-button");
messageInput.addEventListener("keydown", function (event) {
  if (event.key === "Enter") {
      sendButton.click();
      event.preventDefault();
  }
});

function interageComChatbot() {
  const messageInput = document.getElementById("message-input");
  const sendButton = document.getElementById("send-button");
  const messageBox = document.getElementById("message-box");

  const messageText = messageInput.value.trim();

  const newMessage = document.createElement("p");
  newMessage.innerHTML = `<strong>Você:</strong> ${messageText}`;
  messageBox.appendChild(newMessage);
  

  const url = `/chatbot/${messageText}`;

  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      const resposta = data.resposta;
      const anotherMessage = document.createElement("p");
      anotherMessage.innerHTML = `<strong>Chatbot:</strong> ${resposta}`;
      messageBox.appendChild(anotherMessage);
    })
    .catch((error) => {
      console.error('Ocorreu um erro:', error);
    });

    messageInput.value = "";
    messageBox.scrollTop = messageBox.scrollHeight;
};



