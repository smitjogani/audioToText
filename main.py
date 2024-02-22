import speech_recognition as sr
audioFile=("demo.wav")

r = sr.Recognizer()
with sr.AudioFile(audioFile) as source:
    audio = r.record(source)

try:
    print("Audio file content : " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError:
    print("Coudn't get the results from Google cloud speech recognition")