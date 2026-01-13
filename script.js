function sendText() {
  const text = document.getElementById("inputText").value;

  if (text.trim() === "") {
    alert("Please enter your doubt");
    return;
  }

  document.getElementById("analysis").innerText =
    "Analyzing emotion & confusion...";
  document.getElementById("solution").innerText =
    "Please wait...";

  fetch("https://emotion-ai-backend.onrender.com/analyze", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      text: text
    })
  })
  .then(response => response.json())
  .then(data => {
    document.getElementById("analysis").innerText =
      "Emotion: " + data.emotion + " | Confusion Level: " + data.confusion;

    document.getElementById("solution").innerText =
      data.solution;
  })
  .catch(error => {
    document.getElementById("analysis").innerText =
      "Error connecting to server";
    document.getElementById("solution").innerText =
      "Please try again later.";
    console.error(error);
  });
}
