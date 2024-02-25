import speech_recognition as sr
from pydub import AudioSegment
import os

def convert_to_wav(audio_path):
    # Load the audio file
    audio = AudioSegment.from_file(audio_path)

    # Set the output path for the WAV file
    wav_path = os.path.splitext(audio_path)[0] + ".wav"

    # Export the audio to WAV format
    audio.export(wav_path, format="wav")

    return wav_path

def extract_text(audio_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Input the path to the downloaded audio file
audio_path = r"audio\When Steve Jobs predicted the potential of Internet in 1995.mp4"  # Change this to the actual path of your audio file

# Convert the audio file to WAV format
wav_path = convert_to_wav(audio_path)

# Extract text from the WAV file
extracted_text = extract_text(wav_path)

# Print the extracted text
print("Extracted Text:")
print(extracted_text)
