import serial
import time
from flask import Flask, request, redirect
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
def send_text(sendTo,body):
    account_sid = 'AC46368bace24b8dd3f7290ecca8d6e664'
    auth_token = 'ab08351b6999fc8f3123da18e1b60332'
    client = Client(account_sid, auth_token)

    message = client.messages.create(body=body, from_='+12513151614', to=sendTo)

app = Flask(__name__)
@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("The Robots are coming! Head for the hills!")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

def arduino_activated(pn):
    send_text(pn)

BAUD_RATE = 9600
PORT = "COM3"
BYTESIZE = 8
TIMEOUT = 5

PHONE_NUMBER = '+17166501231'

serialPort = serial.Serial(port=PORT, baudrate=BAUD_RATE, timeout=TIMEOUT)

while(True):
    data = serialPort.read(1)
    character = data.decoce("ASCII")
    if (character == 'b'):
        arduino_activated(PHONE_NUMBER)
        break
    time.sleep(1)
