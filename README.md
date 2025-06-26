# 📧 AI Email Auto-Responder
This Python script automatically checks your Gmail inbox, finds the first unread, valid, human-like email, and generates a polite, AI-powered reply using Google's flan-t5-small model.

## ✨ Features
- ✅ Connects securely to Gmail via IMAP

## 📬 Scans all unread emails

- 🧹 Skips marketing, spam, Binance, and empty emails

## 🧠 Uses a Hugging Face Transformer model for smart replies

#### 💬 Prints the sender, subject, **and AI-generated reply**

#### ❌ Skips raw HTML or broken content emails

#### 🛑 Stops after replying to the first valid email

### 🛠️ Requirements
- Install dependencies:

***pip install torch transformers beautifulsoup4***

- Enable IMAP in your Gmail settings

- Create an App Password:

- Visit myaccount.google.com/security

- Enable 2-Step Verification

- Under "App passwords", generate one for "Mail"

- Replace the placeholders in the script:

email_user = 'your_email@gmail.com'                   ***Replace this with your own user***
app_password = 'your_app_password_here'               ***Replace this with your own password using the above steps***
-

## 🚀 How to Run
Just run the script with Python:
**or visit the google colab link:**
***https://colab.research.google.com/drive/1delPABMMdvpnUd1tDH0bDNFiKPr8X52h***

**python main.py
You’ll see output like:**
```bash
-1. 🔁 Loading AI model (flan-t5-small)...
-2. 👤 FROM: John Doe <john@example.com>
-3. 📨 SUBJECT: Need help with login
-4. 🤖 AI SUGGESTED REPLY:
Hi John, I’d be happy to help you regain access to your account. Please try resetting your password from the login screen..
```bash.

### 📂 File Output (Optional)
By default, the script only prints the reply.
If you want to save replies to a file or log, just modify the final section.

#### 🧠 Model Info
This script uses the FLAN-T5 Small model from Hugging Face, known for general-purpose instruction-following tasks.

#### 🔒 Security Notice
Never send with your real Gmail credentials or app password 

## 📌 Future Ideas
✅ Auto-send replies using SMTP

✅ Schedule to run every hour

✅ GUI with Streamlit

✅ Log to CSV or Google Sheet

