from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# 🔥 user session memory
user_data = {}

@app.route("/whatsapp", methods=["POST"])
def whatsapp_bot():

    incoming_msg = request.values.get('Body', '').strip().lower()
    user = request.values.get('From')

    resp = MessagingResponse()
    msg = resp.message()

    # =========================
    # START
    # =========================
    if incoming_msg in ["hi", "hello", "start"]:
        user_data[user] = {"step": "menu"}
        msg.body("👋 Welcome!\nChoose option:\n1️⃣ Book Doctor\n2️⃣ Book Flight")

    # =========================
    # MENU
    # =========================
    elif incoming_msg == "1":
        user_data[user] = {"step": "doctor_name"}
        msg.body("🩺 Enter your name:")

    elif incoming_msg == "2":
        user_data[user] = {"step": "flight_name"}
        msg.body("✈️ Enter your name:")

    # =========================
    # DOCTOR FLOW
    # =========================
    elif user in user_data and user_data[user]["step"] == "doctor_name":
        user_data[user]["name"] = incoming_msg
        user_data[user]["step"] = "doctor_date"
        msg.body("📅 Enter appointment date (YYYY-MM-DD):")

    elif user in user_data and user_data[user]["step"] == "doctor_date":
        name = user_data[user]["name"]
        date = incoming_msg

        msg.body(f"✅ Doctor appointment booked!\nName: {name}\nDate: {date}")

        user_data.pop(user, None)

    # =========================
    # FLIGHT FLOW
    # =========================
    elif user in user_data and user_data[user]["step"] == "flight_name":
        user_data[user]["name"] = incoming_msg
        user_data[user]["step"] = "flight_date"
        msg.body("📅 Enter travel date (YYYY-MM-DD):")

    elif user in user_data and user_data[user]["step"] == "flight_date":
        name = user_data[user]["name"]
        date = incoming_msg

        msg.body(f"✈️ Flight booked!\nName: {name}\nDate: {date}")

        user_data.pop(user, None)

    # =========================
    # INVALID INPUT
    # =========================
    else:
        msg.body("❗ Please type 'hi' to start and choose a valid option (1 or 2)")

    return str(resp)


if __name__ == "__main__":
    app.run(port=5000)