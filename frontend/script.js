async function send() {
  const input = document.getElementById("input").value;

  const res = await fetch("http://localhost:5000/query", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ question: input })
  });

  const data = await res.json();

  document.getElementById("output").innerText =
    data.response || data.error;
}