from flask import Flask, request, jsonify, render_template
import os

# Optional: Only use pyttsx3 in local dev environment
try:
    if os.getenv("ENV") != "production":
        import pyttsx3
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)  # Male voice

        def speak(text):
            print("Nova:", text)
            engine.say(text)
            engine.runAndWait()
    else:
        def speak(text):
            print("Nova:", text)
except ImportError:
    def speak(text):
        print("Nova:", text)

app = Flask(__name__)

# ========== HANDLE COMMAND ==========
def handle_command(query):
    query = query.lower()

    if "who developed you" in query:
        response = "I am developed by Mister Tanay Pandey, he is my only boss and owner."

    elif "search" in query:
        response = f"Searching for '{query.replace('search', '').strip()}' on Google."
        # Suggest a link instead of opening it
        response += " You can try: https://www.google.com/search?q=" + query.replace("search", "").strip().replace(" ", "+")

    elif "open youtube" in query:
        response = "Opening YouTube: https://www.youtube.com"

    elif "open google" in query:
        response = "Opening Google: https://www.google.com"

    elif "open instagram" in query:
        response = "Opening Instagram: https://www.instagram.com"

    elif "open wikipedia" in query:
        response = "Opening Wikipedia: https://www.wikipedia.org"

    elif "open twitter" in query:
        response = "Opening Twitter: https://www.twitter.com"

    elif "open github" in query:
        response = "Opening GitHub: https://www.github.com"

    elif "open whatsapp" in query:
        response = "Opening WhatsApp Web: https://web.whatsapp.com"

    elif "open netflix" in query:
        response = "Opening Netflix: https://www.netflix.com"

    elif "open jnv" in query or "open navodaya" in query:
        response = "Opening Jawahar Navodaya Vidyalaya: https://navodaya.gov.in"

    elif "open facebook" in query:
        response = "Opening Facebook: https://www.facebook.com"

    elif "open amazon" in query:
        response = "Opening Amazon: https://www.amazon.com"

    elif "open reddit" in query:
        response = "Opening Reddit: https://www.reddit.com"

    else:
        response = "Sorry boss, I didn't understand. Please try again."

    speak(response)
    return response

# ========== ROUTES ==========

@app.route("/")
def index():
    return render_template("nova.html")

@app.route("/nova", methods=["POST"])
def nova_command():
    data = request.get_json()
    user_input = data.get("command", "")
    reply = handle_command(user_input)
    return jsonify({"reply": reply})

# ========== MAIN ==========
if __name__ == "__main__":
    print("Nova Flask backend running at http://127.0.0.1:5000")
    speak("Ram Ram Ram Boss!")
    speak("Hey, Nova is ready to assist you, boss!")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
