# 🤖 WhatsApp Chatbot using Twilio + Flask + LLM

A hybrid WhatsApp chatbot built using **Flask** and **Twilio API**, supporting both:

* ✅ Rule-based conversation flow
* 🤖 AI-powered responses using LLM (OpenRouter)

This project demonstrates real-world chatbot development with structured workflows and intelligent AI fallback.

---

## 🚀 Features

* 📱 WhatsApp chatbot using Twilio Sandbox
* 🩺 Doctor Appointment Booking system
* ✈️ Flight Booking system
* 🔁 Multi-step conversational flow
* 🤖 AI fallback for unknown queries
* 🧠 Session-based user tracking
* ⚡ Real-time response handling

---

## 🧠 Chatbot Architectures

### 🔹 1. Rule-Based Chatbot

* Menu-driven interaction
* Fixed conversational flow
* Ideal for structured use cases

### 🔹 2. LLM-Based Chatbot

* Uses OpenRouter API
* Generates dynamic AI responses
* Handles user queries beyond predefined flows

---

## 🗂️ Project Structure

```
whatsapp-chatbot/
│
├── app_with_llm.py        # Chatbot with AI integration
├── app_without_llm.py     # Rule-based chatbot
├── llm.py                 # LLM API logic
├── booking.py             # Booking logic (optional)
├── db.py                  # Database logic (optional)
├── requirements.txt
├── README.md
├── assets/
│   ├── chat1.png
│   └── chat2.png
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/yourusername/whatsapp-chatbot.git
cd whatsapp-chatbot
```

---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Create `.env` File

Create a `.env` file in root directory:

```
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
OPENROUTER_API_KEY=your_openrouter_key
```

⚠️ Never upload `.env` to GitHub

---

### 4️⃣ Run Flask Server

```
python app_with_llm.py
```

Server will start at:

```
http://127.0.0.1:5000
```

---

### 5️⃣ Start ngrok

```
ngrok http 5000
```

Copy HTTPS URL like:

```
https://abcd1234.ngrok-free.app
```

---

### 6️⃣ Configure Twilio Sandbox

* Go to Twilio Console → WhatsApp Sandbox
* Paste webhook URL:

```
https://your-ngrok-url/whatsapp
```

---

## 💬 Sample Chat Outputs

### 📌 Booking Flow (Rule-Based)

![Booking Chat](https://github.com/SinghPriya5/whatsapp-ai-chatbot/blob/main/Booking%20Chat.jpeg)

---

### 📌 AI Chat (LLM Response)

![AI Chat](https://github.com/SinghPriya5/whatsapp-ai-chatbot/blob/main/AI%20Chat.jpeg)

---

## 🎯 How It Works

1. User sends message on WhatsApp
2. Twilio forwards message to Flask webhook
3. Flask processes input
4. Based on logic:

   * Booking flow (rule-based)
   * OR AI response (LLM)
5. Response sent back via Twilio

---

## 🧪 Tech Stack

* Python 🐍
* Flask 🌐
* Twilio API 📱
* OpenRouter (LLM) 🤖
* Ngrok 🔗

---

## 🔥 Key Highlights

* Hybrid chatbot (Rule-based + AI)
* Real-time WhatsApp integration
* Clean and modular architecture
* Beginner to advanced level project
* Demonstrates API + AI integration

---

## 🎯 Use Cases

* Customer Support Bot
* Appointment Booking System
* Travel Assistant
* AI Chat Assistant
* Business Automation

---

## ⚠️ Limitations

* Uses Twilio Sandbox (not production-ready)
* No persistent database (optional enhancement)
* Limited UI (text-based interaction)

---

## 🚀 Future Improvements

* Database integration (MongoDB / MySQL)
* Deployment on cloud (AWS / Render)
* WhatsApp button templates (UI upgrade)
* Multi-language support
* Voice-enabled chatbot

---

## 🎤 Author

**Priya Singh**
Aspiring AI / ML Engineer 🚀

---

## ⭐ Support

If you like this project:

* ⭐ Star the repository
* 🍴 Fork it
* 💬 Share feedback

---
