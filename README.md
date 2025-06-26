# 📧 AI Email Auto-Responder

This Python project automatically fetches the latest **unread email** from your Gmail inbox, analyzes its content, and generates a polite and helpful reply using a **transformer language model** (`flan-t5-small` from Hugging Face).

---

## ✨ Features

- Secure Gmail login using **IMAP and app password**
- Automatically fetches the **latest unread email**
- Extracts **subject**, **sender**, and **email body**
- Uses `google/flan-t5-small` transformer model to **generate smart replies**
- Prints and saves suggested reply to `suggested_reply.txt`

---

## 🚀 Setup & Usage

- 2. Install Required Libraries

- pip install torch transformers
- 3. Gmail Setup
- Go to your Google Account Security

- Enable 2-Step Verification

- Create an App Password for "Mail"

- Use that password in the code:

- email_user = 'your_email@gmail.com'
- app_password = 'your_app_password_here'
- 4. Run the Script

- python main.py
# 💡 How It Works
- Connects to Gmail using IMAP.

- Searches for the most recent unread email.

- Extracts the plain-text or HTML content of the email.

- Feeds it into flan-t5-small with a prompt to generate a smart reply.

- Displays and stores the response in suggested_reply.txt.

# 📂 File Structure

ai-email-auto-responder/
│
├── main.py               # Main script to run
├── suggested_reply.txt   # Stores replies for reference
├── README.md             # You are here!
# 📌 Notes
This project only suggests a reply — it does not send emails automatically.

Works best for simple and short text emails.

Ensure you have a stable internet connection (the model loads from Hugging Face).

# 🧠 Model Used
google/flan-t5-small

A small but powerful model trained for instruction following tasks.
