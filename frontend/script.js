async function askQuestion() {
  const input = document.getElementById("question");
  const chatBox = document.getElementById("chat-box");

  const question = input.value;

  if (!question) {
    return;
  }

  // remove welcome screen after first message
  const welcome = document.querySelector(".welcome");
  const cards = document.querySelector(".cards");

  if (welcome) {
    welcome.remove();
  }

  if (cards) {
    cards.remove();
  }

  // show user message
  chatBox.innerHTML += `
        <div class="message">
            <b>You:</b> ${question}
        </div>
    `;

  // clear input
  input.value = "";

  try {
    const response = await fetch("http://127.0.0.1:8000/ask", {
      method: "POST",

      headers: {
        "Content-Type": "application/json",
      },

      body: JSON.stringify({
        question: question,
        top_k: 5,
      }),
    });

    const data = await response.json();

    // show AI response
    chatBox.innerHTML += `
            <div class="message">
                <b>Travel AI:</b><br>
                ${data.answer.replace(/\n/g, "<br>")}
            </div>
        `;

    // auto scroll down
    chatBox.scrollTop = chatBox.scrollHeight;
  } catch (error) {
    console.log(error);

    chatBox.innerHTML += `
            <div class="message">
                ⚠️ Unable to connect to Travel AI
            </div>
        `;
  }
}

// suggestion buttons
function quickAsk(text) {
  document.getElementById("question").value = text;

  askQuestion();
}

// press Enter to send
document
  .getElementById("question")
  .addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
      askQuestion();
    }
  });
