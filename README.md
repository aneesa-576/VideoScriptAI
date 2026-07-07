# 🎬 VideoScriptAI

> **Generate AI-powered promotional video content in seconds.**
>
> VideoScriptAI is a full-stack AI web application that helps marketers, entrepreneurs, and content creators generate engaging promotional video content using the power of Large Language Models (LLMs). The application generates compelling hooks, promotional scripts, scene suggestions, and call-to-actions tailored to a product and its target audience.

---

## 📖 Overview

Creating promotional videos often requires creativity, marketing expertise, and significant time. VideoScriptAI simplifies this process by using AI to instantly generate high-quality marketing content from a few simple inputs.

The application accepts:

- Product Name
- Product Description
- Target Audience
- Campaign Goal
- Video Duration (Optional)

Using these details, the AI generates:

- 🎯 Hook
- 📜 Promotional Script
- 🎬 Scene Suggestions
- 📢 Call-To-Action (CTA)

This project demonstrates how modern AI can be integrated into a full-stack web application using Flask, REST APIs, JavaScript, and the Groq LLM API.

---

# ✨ Features

## 🎯 AI Hook Generator

Generates a short, attention-grabbing opening line.

### Rules

- Maximum 20 words
- Starts with:
  - A question
  - A surprising fact
  - A bold statement
- Tailored to the selected product and audience

---

## 📜 AI Script Generator

Creates a complete promotional video script.

### Features

- Scene-by-scene formatting
- Voiceover/dialogue included
- Adjustable duration
- Approximately one sentence every three seconds
- 2–3 scenes

---

## 🎬 Scene Suggestion Generator

Generates three visually engaging scene ideas.

Each suggestion includes:

- Camera shot concepts
- Product demonstrations
- Practical visual storytelling
- Marketing-focused scenes

---

## 📢 CTA Generator

Creates a concise, action-oriented closing statement encouraging viewers to purchase or learn more about the product.

---

## 🌐 Interactive Web Interface

- Responsive design
- Modern dark UI
- Loading spinner
- Copy-to-clipboard functionality
- Auto-scroll to generated content
- Dynamic content updates without page refresh

---

## ⚡ REST API Backend

Available API endpoints:

| Method | Endpoint |
|---------|----------|
| GET | `/` |
| POST | `/api/hook` |
| POST | `/api/script` |
| POST | `/api/scenes` |
| POST | `/api/cta` |
| POST | `/api/generate-all` |

---

# 🛠️ Tech Stack

## Backend

- Python
- Flask
- Groq API
- Llama 3.3 70B Versatile
- python-dotenv

## Frontend

- HTML5
- CSS3
- JavaScript (ES6)

## AI

- Prompt Engineering
- Large Language Models (LLMs)
- Groq Inference API

## Version Control

- Git
- GitHub

## Deployment

- Render

---

# 📂 Project Structure

```text
VideoScriptAI/
│
├── ai/
│   ├── client.py
│   ├── hook.py
│   ├── script.py
│   ├── scenes.py
│   └── cta.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/aneesa-576/VideoScriptAI.git

cd VideoScriptAI
```

---

## Create a Virtual Environment

```bash
python -m venv .venv
```

### Activate

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file inside the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

---

## Run the Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

# 🚀 How It Works

1. User enters product details.
2. JavaScript collects the form inputs.
3. Data is sent to the Flask backend using Fetch API.
4. Flask validates the request.
5. A structured AI prompt is created.
6. Prompt is sent to the Groq API.
7. Llama 3.3 generates the requested marketing content.
8. Flask returns the response as JSON.
9. JavaScript dynamically updates the webpage.

---

# 📸 Screenshots

Add screenshots here after deployment.

Suggested screenshots:

- Home Page
- Input Form
- Generated AI Content
- Mobile View

---

# 🌟 Future Enhancements

The project has been designed with scalability and modularity in mind.

Future improvements include:

- Multiple Script Styles
- Generate content in different tones:
- Generate scripts specifically for:
- AI Caption Generator
- Storyboard Generator
- Voice & Music Suggestions
- Export Options
- User Accounts
- Multi-Model AI Support
- Future Scope

VideoScriptAI has the potential to evolve into a comprehensive AI-powered video pre-production platform. Future versions could integrate AI image generation, storyboard visualization, multilingual support, collaborative workspaces, analytics dashboards, and direct integration with popular video editing software. By extending beyond script generation into complete creative planning, VideoScriptAI aims to become an end-to-end assistant for digital marketers, startups, agencies, and content creators.

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository.

2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add feature"
```

4. Push your branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👩‍💻 Author

**Aneesa Shaik**

B.Tech Information Technology Student

Python Developer • AI & Machine Learning Enthusiast

GitHub: https://github.com/aneesa-576

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and supports future development.

---

> **VideoScriptAI** demonstrates how modern AI can automate creative marketing tasks through intelligent prompt engineering and Large Language Models. Built using Flask, Groq LLMs, JavaScript, and modern web technologies, the project serves as both a practical productivity tool and a showcase of full-stack AI application development.