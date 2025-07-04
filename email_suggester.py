# ================================
# 🔐 PASTE YOUR GMAIL CREDENTIALS BELOW 🔐
# 👉 Replace 'Your_email_user' with your Gmail address (with quotes)
# 👉 Replace 'Your_app_password' with the App Password you generated from Google
# ================================

import imaplib
import email
from email.header import decode_header
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import os

# ========== 1. GMAIL LOGIN ==========
email_user = 'Your_email_user'
app_password = 'Your_app_password'  # App password from Google

try:
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(email_user, app_password)
    mail.select('inbox')
except Exception as e:
    print(f"❌ Login error: {e}")
    exit()

# ... (rest of your original code is unchanged)
