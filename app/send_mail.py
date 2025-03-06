from mailjet_rest import Client
from app.config import MAILJET_API_KEY, MAILJET_SECRET_KEY, MAILJET_SENDER

def send_email(to_email, template_id, link):
    mailjet = Client(auth=(MAILJET_API_KEY, MAILJET_SECRET_KEY), version='v3.1')

    data = {
        "Messages": [
            {
                "From": {"Email": MAILJET_SENDER, "Name": "Ecor Rouge"},
                "To": [{"Email": to_email, "Name": to_email.split('@')[0]}],
                "TemplateID": template_id,
                "TemplateLanguage": True,
                "Variables": {"verify_link": link}
            }
        ]
    }

    response = mailjet.send.create(data=data)

    if response.status_code == 200:
        return True
    else:
        print(f"Failed to send email: {response.json()}")
        return False
