#(251) 315-1614

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC46368bace24b8dd3f7290ecca8d6e664'
auth_token = 'ab08351b6999fc8f3123da18e1b60332'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+12513151614',
                     to='+17162085357'
                 )

print(message.sid)


def rest():
    return None