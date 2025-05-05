from flask import Flask, render_template, request, jsonify
import pyttsx3

app = Flask(__name__)

# Initialize Text-to-Speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def handle_command(query):
    query = query.lower()
    url = None

    if "hello" in query:
        response = "Hello boss, how can I help you?"
    elif "how are you" in query:
        response = "I'm doing great, boss. Ready to help you anytime!"
    elif "open youtube" in query:
        response = "Opening YouTube, boss!"
        url = "https://www.youtube.com"
    elif "open google" in query:
        response = "Opening Google, boss!"
        url = "https://www.google.com"
    elif "open github" in query:
        response = "Opening GitHub, boss!"
        url = "https://github.com"
    elif "thank you" in query or "thanks" in query:
        response = "You're welcome, boss!"
    else:
        response = "Sorry boss, I didn't understand. Please try again."

    return response, url

@app.route("/")
def index():
    return render_template("nova.html")

@app.route("/nova", methods=["POST"])
def nova_command():
    data = request.get_json()
    user_input = data.get("command", "")
    reply, url = handle_command(user_input)
    return jsonify({"reply": reply, "url": url})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
