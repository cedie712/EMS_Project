# import pyttsx3 as talk
import speech_recognition as sr
# import signal


class Speech:
    def capture(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            try:
                audio = r.listen(source, timeout=5)


                try:
                    cap = r.recognize_google(audio)
                    if 'sign in' in cap or 'sign me in' in cap or 'clock in' in cap:
                        print(cap)
                        return 'clock-in'
                    elif 'sign out' in cap or 'sign me out' in cap or 'clock out' in cap:
                        print(cap)
                        return 'clock-out'
                    elif 'show logs' or 'my' in cap:
                        print(cap)
                        return 'show my logs'
                    elif 'show all logs' in cap:
                        print(cap)
                        return 'show all logs'
                    else:
                        print(cap)
                        return 'unknown command'
                except sr.UnknownValueError:
                    return "Could not understand audio"
                except sr.RequestError as e:
                    return "Could not request results from Google Speech Recognition service; {0}".format(e)
            except sr.WaitTimeoutError:
                return 'listening time-out'


