from flask import Flask, render_template, request
from twilio.rest import Client
from datetime import datetime

app = Flask(__name__)

# Twilio credentials
account_sid = 'YOUR_SID'
auth_token = 'YOUR_AUTH_TOKEN'
twilio_number = '+YOUR_TWILIO_PHONE'
owner_number = '+91YOUR_PHONE'

client = Client(account_sid, auth_token)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        time_now = datetime.now().strftime('%d-%m-%Y %I:%M %p')

        message_body = f"🚪 Visitor Alert:\nName: {name}\nTime: {time_now}"

        client.messages.create(
            body=message_body,
            from_=twilio_number,
            to=owner_number
        )

        return f"Thanks {name}, your visit has been recorded."

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)