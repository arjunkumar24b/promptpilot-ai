const API_URL = "https://promptpilot-ai-d46a.onrender.com";


// ---------------- LOGIN / SIGNUP MODALS ----------------

function showLogin() {
    document.getElementById(
        "loginModal"
    ).style.display = "block";
}

function showSignup() {
    document.getElementById(
        "signupModal"
    ).style.display = "block";
}


// ---------------- SIGNUP ----------------

async function signupUser() {

    const username =
        document.getElementById(
            "signupUsername"
        ).value;

    const email =
        document.getElementById(
            "signupEmail"
        ).value;

    const password =
        document.getElementById(
            "signupPassword"
        ).value;

    try {

        const response = await fetch(
            `${API_URL}/signup`,
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({
                    username,
                    email,
                    password
                })
            }
        );

        const data = await response.json();

        alert(data.message);

        document.getElementById(
            "signupModal"
        ).style.display = "none";

    } catch (error) {

        alert(
            "Signup failed. Please try again."
        );
    }
}


// ---------------- LOGIN ----------------

async function loginUser() {

    const email =
        document.getElementById(
            "loginEmail"
        ).value;

    const password =
        document.getElementById(
            "loginPassword"
        ).value;

    try {

        const response = await fetch(
            `${API_URL}/login`,
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({
                    email,
                    password
                })
            }
        );

        const data = await response.json();

        if (data.access_token) {

            localStorage.setItem(
                "token",
                data.access_token
            );

            alert("Login successful!");

            document.getElementById(
                "loginModal"
            ).style.display = "none";

        } else {

            alert(
                data.message ||
                "Invalid credentials"
            );
        }

    } catch (error) {

        alert(
            "Login failed. Please try again."
        );
    }
}


// ---------------- GENERATE PROMPT ----------------

async function generatePrompt() {

    const userInput =
        document.getElementById(
            "userInput"
        ).value;

    const platform =
        document.getElementById(
            "platform"
        ).value;

    const style =
        document.getElementById(
            "style"
        ).value;

    const resultBox =
        document.getElementById(
            "result"
        );

    if (!userInput.trim()) {

        alert(
            "Please enter your query."
        );

        return;
    }

    resultBox.innerHTML =
        "⏳ Generating optimized prompt...";

    try {

        const token =
            localStorage.getItem("token");

        const headers = {
            "Content-Type":
                "application/json"
        };

        if (token) {

            headers["Authorization"] =
                `Bearer ${token}`;
        }

        const response = await fetch(
            `${API_URL}/optimize`,
            {
                method: "POST",
                headers: headers,

                body: JSON.stringify({
                    user_input: userInput,
                    platform: platform,
                    style: style
                })
            }
        );

        if (!response.ok) {

            throw new Error(
                "Failed to generate prompt."
            );
        }

        const data =
            await response.json();

        let output = `
            <h3>✨ Optimized Prompt</h3>
            <pre>${data.result}</pre>

            <h3>📊 Quality Score</h3>
            <p>${data.quality_score}/100</p>
        `;

        if (!data.saved) {

            output += `
                <div
                    style="
                        margin-top:20px;
                        padding:15px;
                        background:#fff3cd;
                        border-radius:8px;
                    "
                >

                🔒 Login or Sign Up to save
                prompts and access history.

                </div>
            `;
        } else {

            output += `
                <div
                    style="
                        margin-top:20px;
                        padding:15px;
                        background:#d4edda;
                        border-radius:8px;
                    "
                >

                ✅ Prompt saved to history.

                </div>
            `;
        }

        resultBox.innerHTML = output;

    } catch (error) {

        console.error(error);

        resultBox.innerHTML = `
            <p style="color:red;">

                ❌ Error:
                Could not connect to server.

            </p>
        `;
    }
}