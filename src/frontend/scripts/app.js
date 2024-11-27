document.getElementById('submit-query').addEventListener('click', async () => {
    const query = document.getElementById('user-query').value.trim();
    if (!query) {
        alert('Please enter a query!');
        return;
    }

    try {
        const response = await fetch('http://localhost:5000/chatbot', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query })
        });

        if (response.ok) {
            const data = await response.json();
            document.getElementById('retrieved-info').textContent = data.relevantChunks.join('\n');
        } else {
            document.getElementById('retrieved-info').textContent = 'Error: Unable to fetch response.';
        }
    } catch (error) {
        document.getElementById('retrieved-info').textContent = `Error: ${error.message}`;
    }
});
