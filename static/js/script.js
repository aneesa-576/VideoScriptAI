
const generateBtn = document.getElementById("generateBtn");

// ===============================
// VideoScriptAI Frontend Logic
// ===============================

const form = document.getElementById("videoForm");
const loadingMessage = document.getElementById("loadingMessage");

// Output elements
const hookResult = document.getElementById("hookResult");
const scriptResult = document.getElementById("scriptResult");
const scenesResult = document.getElementById("scenesResult");
const ctaResult = document.getElementById("ctaResult");


// ======================================
// Handle Form Submission
// ======================================

form.addEventListener("submit", async function (event) {

    event.preventDefault();

    loadingMessage.style.display = "flex";

    generateBtn.disabled = true;
    generateBtn.textContent = "Generating...";

    hookResult.textContent = "Generating...";
    scriptResult.textContent = "Generating...";
    scenesResult.textContent = "Generating...";
    ctaResult.textContent = "Generating...";

    const payload = {

        product: document.getElementById("product").value,

        description: document.getElementById("description").value,

        audience: document.getElementById("audience").value,

        goal: document.getElementById("goal").value,

        duration: document.getElementById("duration").value

    };

    try {

        const response = await fetch("/api/generate-all", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(payload)

        });

        const data = await response.json();

        loadingMessage.style.display = "none";

        if (!response.ok) {

            alert(data.error);

            return;

        }

        hookResult.textContent = data.hook;
        scriptResult.textContent = data.script;
        scenesResult.textContent = data.scenes;
        ctaResult.textContent = data.cta;

        // Re-enable the button
        generateBtn.disabled = false;
        generateBtn.innerHTML = "Generate Content 🚀";
        
        document.getElementById("results").scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
        

    }
 

    catch (error) {

        loadingMessage.style.display = "none";
        generateBtn.disabled = false;
        generateBtn.textContent = "Generate Content 🚀";
        alert("Something went wrong!");

        console.error(error);

    }

});


// ======================================
// Copy Buttons
// ======================================

document.querySelectorAll(".copy-btn").forEach(button => {

    button.addEventListener("click", () => {

        const target = document.getElementById(
            button.dataset.copy
        );

        navigator.clipboard.writeText(target.textContent);

        button.textContent = "Copied!";

        setTimeout(() => {

            button.textContent = "Copy";

        }, 1500);

    });

});