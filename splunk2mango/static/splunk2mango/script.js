function copyToClipboard() {
    const text = document.getElementById('jsonOutput').innerText;
    navigator.clipboard.writeText(text).then(function() {
        // Change the button text to "Copied!"
        const copyButton = document.getElementById('copyButton');
        copyButton.textContent = 'Copied!';
        // After 1 second, revert the text back to "Copy Code"
        setTimeout(() => {
            copyButton.textContent = 'Copy Code';
        }, 1000);
    }, function(err) {
        console.error('Could not copy text: ', err);
    });
}
