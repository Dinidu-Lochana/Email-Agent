from vosk import Model, KaldiRecognizer
import pyaudio
import json

def transcribe_voice():
    model = Model("vosk-model-small-en-us-0.15")  # path to unzipped model
    recognizer = KaldiRecognizer(model, 16000)

    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000,
                      input=True, frames_per_buffer=8192)
    print("🎤 Speak something...")

    stream.start_stream()
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            break

    stream.stop_stream()
    stream.close()
    mic.terminate()

    text = json.loads(result).get("text", "")
    print("📝 Transcribed Text:", text)
    return text

if __name__ == "__main__":
    transcribe_voice()
