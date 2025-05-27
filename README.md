# 📱 SMS API Spoofer

**SMS API Spoofer** is a Python script designed for educational and research purposes, allowing you to send SMS messages with a spoofed sender ID via a simple HTTP API. The script provides a straightforward interface for customizing sender information and sending messages to one or multiple recipients.

---

## 🚀 Features

- **Easy to Use:** Simple Python script, no advanced programming required.
- **Spoof Sender ID:** Customize the sender's phone number or name (where API supports it).
- **Bulk Messaging:** Supports for sending messages to multiple recipients.
- **API Integration:** Sends requests to `http://toolsbuy.org/wsms`.
- **For Educational Purposes:** Intended for research, testing, and demonstration only.

---

## 🙋‍♂️ Need Help?  
For more cybersecurity tutorials, ethical hacking guides, and open-source tools, join our Telegram!

<a href="https://t.me/toolsbuy" target="_blank">
  <img src="https://img.shields.io/badge/👤 Chat%20on%20Telegram-blue?style=for-the-badge" alt="Chat on Telegram" />
</a>

## ⚡ Getting Started

### Prerequisites

- Python 3.7+ ([Download Python](https://www.python.org/downloads/))
- `pip` package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/toolsbuy-org/sms-api-spoofer.git
   cd sms-api
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🛠️ Usage

Edit `main.py` with your desired parameters or run as is for a test example.

```python
from main import send_spoofed_sms

api_url = "http://toolsbuy.org/wsms"
sender = "+10000000000" or "SpoofedSender" 
recipient = "+1234567890"
message = "This is a test spoofed SMS sent using Python."


send_spoofed_sms(api_url, sender, recipient, message)
```

Or simply run:
```bash
python main.py
```

---

## 📚 Example

The script sends a POST request to `http://toolsbuy.org/wsms` with the following parameters:

- `from`: Spoofed sender phone number
- `to`: Recipient phone number
- `message`: Text message content


---

## ⚠️ Disclaimer

> **This tool is for educational and research purposes only.**  
> Do not use for any malicious, illegal, or unethical activities.  
> You are responsible for complying with all local laws and regulations.

---

## 📄 License

See [LICENSE](LICENSE) for full details.

---
