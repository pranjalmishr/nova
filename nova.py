# from flask import Flask, request, jsonify, render_template
# import os
# import webbrowser

# app = Flask(__name__)
# USE_TTS = os.getenv("ENV") != "production"

# # ========== TEXT TO SPEECH ==========
# if USE_TTS:
#     try:
#         import pyttsx3
#         engine = pyttsx3.init()
#         voices = engine.getProperty('voices')
#         engine.setProperty('voice', voices[0].id)  # Male voice

#         def speak(text):
#             print("Nova:", text)
#             engine.say(text)
#             engine.runAndWait()
#     except Exception as e:
#         print("Speech engine init failed:", e)

#         def speak(text):
#             print("Nova:", text)
# else:
#     def speak(text):
#         print("Nova:", text)

# # ========== HANDLE COMMAND ==========
# def handle_command(query):
#     query = query.lower()

#     if "who developed you" in query:
#         response = "I am developed by Mister Tanay Pandey, he is my only boss and owner."

#     elif "open youtube" in query:
#         webbrowser.open("https://www.youtube.com")
#         response = "Opening YouTube, boss!"

#     elif "open google" in query:
#         webbrowser.open("https://www.google.com")
#         response = "Opening Google, boss!"

#     elif "open instagram" in query:
#         webbrowser.open("https://www.instagram.com")
#         response = "Opening Instagram, boss!"

#     elif "open wikipedia" in query:
#         webbrowser.open("https://www.wikipedia.org")
#         response = "Opening Wikipedia, boss!"

#     elif "open twitter" in query:
#         webbrowser.open("https://www.twitter.com")
#         response = "Opening Twitter, boss!"

#     elif "open github" in query:
#         webbrowser.open("https://www.github.com")
#         response = "Opening GitHub, boss!"

#     elif "open whatsapp" in query:
#         webbrowser.open("https://web.whatsapp.com")
#         response = "Opening WhatsApp Web, boss!"

#     elif "open netflix" in query:
#         webbrowser.open("https://www.netflix.com")
#         response = "Opening Netflix, boss!"

#     elif "open jnv" in query or "open navodaya" in query:
#         webbrowser.open("https://navodaya.gov.in")
#         response = "Opening Jawahar Navodaya Vidyalaya Samiti website, boss!"

#     elif "open facebook" in query:
#         webbrowser.open("https://www.facebook.com")
#         response = "Opening Facebook, boss!"

#     elif "open amazon" in query:
#         webbrowser.open("https://www.amazon.com")
#         response = "Opening Amazon, boss!"

#     elif "open reddit" in query:
#         webbrowser.open("https://www.reddit.com")
#         response = "Opening Reddit, boss!"

#     else:
#         response = "Sorry boss, I didn't understand. Please try again."

#     speak(response)
#     return response

# # ========== ROUTES ==========
# @app.route("/")
# def index():
#     return render_template("nova.html")

# @app.route("/nova", methods=["POST"])
# def nova_command():
#     data = request.get_json()
#     user_input = data.get("command", "")
#     reply = handle_command(user_input)
#     return jsonify({"reply": reply})

# # ========== MAIN ==========
# import os

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host="0.0.0.0", port=port)

from flask import Flask, render_template, request, jsonify
import webbrowser
import datetime
import os

app = Flask(__name__)

# --- Core logic ---
def handleCommand(command):
    command = command.lower()

    if "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google."

    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The current time is {now}."

    elif "date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        return f"Today's date is {today}."

    else:
        return "Sorry, I didn't understand that command."

# --- Routes ---
@app.route("/")
def index():
    return render_template("nova.html")

@app.route("/nova", methods=["POST"])
def nova_response():
    data = request.get_json()
    user_input = data.get("query", "")

    response = handleCommand(user_input)

    return jsonify({"response": response})

# --- Entry point ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
