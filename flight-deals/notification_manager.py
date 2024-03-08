import json
from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        with open('../config.json') as f:
            config_data = json.load(f)
        self.email_host = config_data["email"]["host"]
        self.email_port = config_data["email"]["port"]
        self.email_sender = config_data["email"]["sender"]
        self.email_password = config_data["email"]["password"]
        self.sms_account_sid = config_data["twilio"]["account_sid"]
        self.sms_auth_token = config_data["twilio"]["auth_token"]
        self.sms_sender_mob = config_data["twilio"]["sender_mob"]

    def send_email(self, receiver, message):
        pass

    def send_sms(self, receiver, message):
        client = Client(self.sms_account_sid, self.sms_auth_token)
        message = client.messages.create(
            body=message,
            from_='+19309662195',
            to=receiver
        )
        return message.sid
