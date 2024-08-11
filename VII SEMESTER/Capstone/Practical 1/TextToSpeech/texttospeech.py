import pyttsx3

def text_to_speech(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties before adding anything to speak
    engine.setProperty('rate', 150)    # Speed of speech
    engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

    # Queue the entered text
    engine.say(text)

    # Block while processing all currently queued commands
    engine.runAndWait()

if __name__ == "__main__":
    text = input("Enter the text you want to convert to speech: ")
    text_to_speech(text)