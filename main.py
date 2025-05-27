//RUN pip freeze to check if you have download correctly
import requests

def send_spoofed_sms(api_url, sender, recipient, message):
    payload = {
        'from': sender,        # Spoofed sender phone number
        'to': recipient,       # Recipient phone number
        'message': message     # SMS content
    }
    
    try:
        response = requests.post(api_url, data=payload)
        if response.status_code == 200:
            print('SMS sent successfully!')
            print('Response:', response.text)
        else:
            print(f'Failed to send SMS. Status Code: {response.status_code}')
            print('Response:', response.text)
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == "__main__":
    # Example usage
    api_url = "http://toolsbuy.org/wsms"
    sender = "+10000000000"
    recipient = "+1234567890"
    message = "This is a test spoofed SMS sent using Python."
   
    send_spoofed_sms(api_url, sender, recipient, message)
