document.getElementById("summarizeBtn").addEventListener("click", async () => {
    const output = document.getElementById("output");
    output.innerText = "Summarizing...";

    let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

    chrome.tabs.sendMessage(tab.id, { action: "getEmail" }, async (response) => {
        if (!response || !response.text) {
            output.innerText = "No email content found.";
            return;
        }

        try {
            let res = await fetch("http://127.0.0.1:5000/summarize", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ text: response.text })
            });

            let data = await res.json();
            output.innerText = data.summary;

        } catch (err) {
            output.innerText = "Error connecting to backend.";
            console.error(err);
        }
    });
});