import random
import time
import speech_recognition as sr
# harvard = sr.AudioFile('Desktop/temp/speechfile/audio_files/harvard.wav')
# with harvard as source:
#     audio = r.record(source)
# print(type(audio))
# print(r.recognize_google(audio))
# jackhammer = sr.AudioFile('Desktop/temp/speechfile/audio_files/jackhammer.wav')
# with jackhammer as source:
#     r.adjust_for_ambient_noise(source, duration = 0.5)
#     audio = r.record(source)
# print(r.recognize_google(audio, show_all = True))
# mic = sr.Microphone(device_index = 0)
# print(sr.Microphone.list_microphone_names())
# with mic as source:
#     r.adjust_for_ambient_noise(source)
#     audio = r.listen(source)
# print(r.recognize_google(audio))
def recognize_speech_from_mic(recognizer,microphone):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")
    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"
    return response

if __name__== "__main__":
    r = sr.Recognizer()
    m = sr.Microphone()
    print('Say something')
    running = 1
    while running:
        guess = recognize_speech_from_mic(r,m)
        if guess['success'] == True:
            print("You said: {}".format(guess["transcription"]))
        else:
            print("Sorry I didnt catch it")