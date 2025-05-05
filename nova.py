from flask import Flask, request, jsonify, render_template
import pyttsx3
import webbrowser
# from googlesearch import search

app = Flask(__name__)

# ========== TEXT TO SPEECH ==========
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Male voice

def speak(text):
    print("Nova:", text)
    engine.say(text)
    engine.runAndWait()

# ========== HANDLE COMMAND ==========
def handle_command(query):
    query = query.lower()
    if "who developed you" in query:
        response = "I am developed by Mister Tanay Pandey, he is my only boss and owner."

    elif "search" in query:
        response = "Searching on Google, boss!"
        query = query.replace("search", "")
        for j in search(query, num=1, stop=1, pause=2):
            webbrowser.open(j)
            break

    elif "open youtube" in query:
        webbrowser.open("https://www.youtube.com")
        response = "Opening YouTube, boss!"

    elif "open google" in query:
        webbrowser.open("https://www.google.com")
        response = "Opening Google, boss!"

    elif "open instagram" in query:
        webbrowser.open("https://www.instagram.com")
        response = "Opening Instagram, boss!"

    elif "open wikipedia" in query:
        webbrowser.open("https://www.wikipedia.org")
        response = "Opening Wikipedia, boss!"

    elif "open twitter" in query:
        webbrowser.open("https://www.twitter.com")
        response = "Opening Twitter, boss!"

    elif "open github" in query:
        webbrowser.open("https://www.github.com")
        response = "Opening GitHub, boss!"

    elif "open whatsapp" in query:
        webbrowser.open("https://web.whatsapp.com")
        response = "Opening WhatsApp Web, boss!"

    elif "open netflix" in query:
        webbrowser.open("https://www.netflix.com")
        response = "Opening Netflix, boss!"

    elif "open jnv" in query or "open navodaya" in query:
        webbrowser.open("https://navodaya.gov.in")
        response = "Opening Jawahar Navodaya Vidyalaya Samiti website, boss!"

    elif "open facebook" in query:
        webbrowser.open("https://www.facebook.com")
        response = "Opening Facebook, boss!"

    elif "open amazon" in query:
        webbrowser.open("https://www.amazon.com")
        response = "Opening Amazon, boss!"

    elif "open reddit" in query:
        webbrowser.open("https://www.reddit.com")
        response = "Opening Reddit, boss!"

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
    speak(" ram Ram Ram Boss!")
    speak(" hey Nova is ready to assist you boss!")
    app.run(debug=True)
