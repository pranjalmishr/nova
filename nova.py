from flask import Flask, render_template, request, jsonify
import webbrowser
import datetime
import pyttsx3

app = Flask(__name__)

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print("Nova says:", text)
    engine.say(text)
    engine.runAndWait()

# Function to handle commands
def handle_command(command):
    command = command.lower()
    response = "Sorry, I didn't understand that."

    if "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        response = "Opening YouTube."

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        response = "Opening Google."

    elif "what time" in command or "tell me the time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        response = f"The current time is {now}."

    elif "search" in command:
        query = command.replace("search", "").strip()
        if query:
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            response = f"Searching Google for {query}."
        else:
            response = "What would you like me to search?"

    elif "play music" in command:
        webbrowser.open("https://open.spotify.com")
        response = "Playing music on Spotify."

    elif "hello" in command or "hi" in command:
        response = "Hello! How can I assist you today?"

    speak(response)
    return response

# Routes
@app.route('/')
def index():
    return render_template('nova.html')

@app.route('/nova', methods=['POST'])
def nova_response():
    user_input = request.form['user_input']
    response = handle_command(user_input)
    return jsonify({'response': response})

# Run app on Render
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
