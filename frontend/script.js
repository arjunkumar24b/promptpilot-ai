const API_URL = "https://promptpilot-ai-d46a.onrender.com";

async function generatePrompt() {
    const userInput = document.getElementById("userInput").value;
    const platform = document.getElementById("platform").value;
    const style = document.getElementById("style").value;

    const resultBox = document.getElementById("result");

    // Validation
    if (!userInput.trim()) {
        alert("Please enter your problem or query.");
        return;
    }

    resultBox.innerHTML = "⏳ Generating optimized prompt...";

    try {
        const response = await fetch(`${API_URL}/optimize`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                user_input: userInput,
                platform: platform,
                style: style
            }),
        });

        if (!response.ok) {
            throw new Error("Failed to generate prompt.");
        }

        const data = await response.json();

        // Handle both old and new response formats
        let output = "";

        if (data.result) {
            output = `
                <h3>✨ Optimized Prompt</h3>
                <pre>${data.result}</pre>
            `;
        } else {
            output = `
                <h3>📂 Category</h3>
                <p>${data.category}</p>

                <h3>✨ Optimized Prompt</h3>
                <pre>${data.optimized_prompt}</pre>

                <h3>📊 Quality Score</h3>
                <p>${data.quality_score || "N/A"}/100</p>

                <h3>💡 Tips</h3>
                <ul>
                    ${data.tips.map(tip => `<li>${tip}</li>`).join("")}
                </ul>
            `;
        }

        resultBox.innerHTML = output;

    } catch (error) {
        console.error(error);
        resultBox.innerHTML = `
            <p style="color:red;">
                ❌ Error: Could not connect to the server.
                Please try again after a few seconds.
            </p>
        `;
    }
}