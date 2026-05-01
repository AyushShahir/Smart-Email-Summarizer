function getEmailContent() {
    let email = document.querySelector('.a3s'); // Gmail email body
    return email ? email.innerText : "No email found";
}

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "getEmail") {
        sendResponse({ text: getEmailContent() });
    }
});