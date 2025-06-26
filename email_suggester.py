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

# ========== 2. SEARCH UNREAD EMAILS ==========
status, data = mail.search(None, 'UNSEEN')
email_ids = data[0].split()

if not email_ids:
    print("📭 No unread emails found.")
    exit()

latest_email_id = email_ids[-1]
status, msg_data = mail.fetch(latest_email_id, '(RFC822)')
msg = email.message_from_bytes(msg_data[0][1])

# ========== 3. EXTRACT EMAIL INFO ==========
def decode_header_value(header_val):
    decoded, charset = decode_header(header_val)[0]
    if isinstance(decoded, bytes):
        return decoded.decode(charset or 'utf-8', errors='ignore')
    return decoded

subject = decode_header_value(msg['subject'])
sender = decode_header_value(msg['from'])

# ========== 4. EXTRACT BODY ==========
def get_email_body(msg):
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))
            if "attachment" in content_disposition:
                continue
            if content_type == "text/plain":
                return part.get_payload(decode=True).decode('utf-8', errors='ignore')
            elif content_type == "text/html":
                html = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                # Optionally strip HTML tags or convert to plain text
                return html
    else:
        return msg.get_payload(decode=True).decode('utf-8', errors='ignore')
    return "[No body found]"

email_body = get_email_body(msg)

# ========== 5. LOAD TRANSFORMER MODEL ==========
print("🔁 Loading AI model (flan-t5-small)...")
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")

# ========== 6. GENERATE AI REPLY ==========
prompt = f"Write a short, helpful and polite reply to this email:\n\n{email_body}"
inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
outputs = model.generate(inputs["input_ids"], max_new_tokens=100)

ai_reply = tokenizer.decode(outputs[0], skip_special_tokens=True)

# ========== 7. DISPLAY & SAVE ==========
print("\n📧 SUBJECT:", subject)
print("👤 FROM:", sender)
print("\n📝 EMAIL BODY:\n", email_body)
print("\n🤖 AI SUGGESTED REPLY:\n", ai_reply)

# Save to file
with open("suggested_reply.txt", "a", encoding="utf-8") as f:
    f.write("="*40 + "\n")
    f.write(f"Subject: {subject}\nFrom: {sender}\n\n")
    f.write("Original Email:\n" + email_body.strip() + "\n\n")
    f.write("Suggested AI Reply:\n" + ai_reply.strip() + "\n\n")

