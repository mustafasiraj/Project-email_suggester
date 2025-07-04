# 📧 AI Email Auto-Responder

This Python script automatically checks your Gmail inbox, finds the first unread, valid, human-like email, and generates a polite, AI-powered reply using Google's `flan-t5-small` model.  
🧠 *Note: The replies are generally good, but always review before sending.*

---

## Notes:
- **please enter your own credidentials in the code like** 
- **Email_user: YOUR_EMAIL_USER**
- **App_password: YOUR_APP_PASSWORD**

## ✨ Features

- ✅ Connects securely to Gmail via IMAP  
- 📬 Scans all unread emails  
- 🧹 Skips marketing, spam, Binance, and empty emails  
- 🧠 Uses a Hugging Face transformer model for smart replies  
- 💬 Shows the sender, subject, **and AI-generated reply**  
- ❌ Skips raw HTML or broken content emails  
- 🛑 Stops after replying to the first valid email  

---

## 🛠️ Requirements

### 1. Install Dependencies
```bash
pip install torch transformers beautifulsoup4
