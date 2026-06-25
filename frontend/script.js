async function generatePrompt() {

    document.getElementById("loading").innerText =
        "Generating prompt...";

    const userInput =
        document.getElementById("userInput").value;

    const platform =
        document.getElementById("platform").value;

    const style =
        document.getElementById("style").value;

    const response = await fetch(
        "http://127.0.0.1:8000/optimize",
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                user_input: userInput,
                platform: platform,
                style: style
            })
        }
    );

    const data = await response.json();

    document.getElementById("loading").innerText = "";

    document.getElementById("result").innerText =
        data.result +
        "\n\nQuality Score: " +
        data.quality_score + "/100";
}


function copyPrompt() {

    const text =
        document.getElementById("result").innerText;

    navigator.clipboard.writeText(text);

    alert("Prompt copied successfully!");
}