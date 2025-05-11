from vosk import Model, KaldiRecognizer
import pyaudio
import json

def transcribe_voice():
    model = Model("vosk-model-small-en-us-0.15")
    recognizer = KaldiRecognizer(model, 16000)
    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000,
                      input=True, frames_per_buffer=8192)
    print("🎙️ Speak now...")
    stream.start_stream()

    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            break

    text = json.loads(result)['text']
    print("📝 You said:", text)
    stream.stop_stream()
    stream.close()
    mic.terminate()
    return text
