import pyttsx3
import speech_recognition as sr


def speak(text):
    """
    Outputs the text in audio
    :param text: Text from audio input
    :return: Text in audio
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def get_audio():
    """
    Gets the input audio
    :return: Audio in text format
    """
    recogn = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recogn.listen(source)
        said = ""

        try:
            said = recogn.recognize_google(audio)
        except Exception as e:
            print("Exception", str(e))
    return said.lower()
