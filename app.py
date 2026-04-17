from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from llm import call_llm
from db import init_db, save_booking

app = Flask(__name__)

# init database
init_db()

user_data = {}

@app.route("/whatsapp", methods=["POST"])
def whatsapp_bot():

    incoming_msg = request.values.get('Body', '').strip().lower()
    user = request.values.get('From')

    resp = MessagingResponse()
    msg = resp.message()

    # START
    if incoming_msg in ["hi", "hello", "start"]:
        user_data[user] = {"step": "menu"}
        msg.body("👋 Welcome!\n1️⃣ Book Doctor\n2️⃣ Book Flight")

    # MENU
    elif incoming_msg in ["1", "book doctor"]:
        user_data[user] = {"step": "doctor_name"}
        msg.body("🩺 Enter your name:")

    elif incoming_msg in ["2", "book flight"]:
        user_data[user] = {"step": "flight_name"}
        msg.body("✈️ Enter your name:")

    # DOCTOR FLOW
    elif user in user_data and user_data[user]["step"] == "doctor_name":
        user_data[user]["name"] = incoming_msg
        user_data[user]["step"] = "doctor_date"
        msg.body("📅 Enter appointment date:")

    elif user in user_data and user_data[user]["step"] == "doctor_date":
        name = user_data[user]["name"]
        date = incoming_msg

        save_booking(name, "Doctor", date)

        msg.body(f"✅ Doctor appointment booked!\nName: {name}\nDate: {date}")

    # FLIGHT FLOW
    elif user in user_data and user_data[user]["step"] == "flight_name":
        user_data[user]["name"] = incoming_msg
        user_data[user]["step"] = "flight_date"
        msg.body("📅 Enter travel date:")

    elif user in user_data and user_data[user]["step"] == "flight_date":
        name = user_data[user]["name"]
        date = incoming_msg

        save_booking(name, "Flight", date)

        msg.body(f"✈️ Flight booked!\nName: {name}\nDate: {date}")

    # AI fallback
    else:
        try:
            reply = call_llm(incoming_msg)
            msg.body(reply)
        except:
            msg.body("❗ Type 'hi' to start")

    return str(resp)


if __name__ == "__main__":
    app.run(port=5000)