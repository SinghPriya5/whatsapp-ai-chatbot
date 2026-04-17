from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from llm import call_llm   # 🔥 LLM import

app = Flask(__name__)

user_data = {}

@app.route("/whatsapp", methods=["POST"])
def whatsapp_bot():

    incoming_msg = request.values.get('Body', '').strip().lower()
    user = request.values.get('From')

    resp = MessagingResponse()
    msg = resp.message()

    # =========================
    # START MENU
    # =========================
    if incoming_msg in ["hi", "hello", "start"]:
        user_data[user] = {"step": "menu"}

        msg.body(
            "👋 Welcome!\n\n"
            "Please choose an option:\n\n"
            "1️⃣ Book Doctor\n"
            "2️⃣ Book Flight\n"
            "💬 Or ask anything (AI)"
        )

    # =========================
    # MENU SELECT
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

        msg.body(
            f"✅ Appointment Confirmed!\n\n"
            f"👤 Name: {name}\n"
            f"📅 Date: {date}\n\n"
            f"Type 'hi' to restart"
        )

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

        msg.body(
            f"✈️ Flight Confirmed!\n\n"
            f"👤 Name: {name}\n"
            f"📅 Date: {date}\n\n"
            f"Type 'hi' to restart"
        )

        user_data.pop(user, None)

    # =========================
    # LLM FALLBACK (IMPORTANT)
    # =========================
    else:
        reply = call_llm(incoming_msg)
        msg.body(reply)

    return str(resp)


if __name__ == "__main__":
    app.run(port=5000)