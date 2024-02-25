from pytube import YouTube

def download_audio(youtube_url, output_path):
    try:
        # Create a YouTube object
        yt = YouTube(youtube_url)
        
        # Get the highest quality audio stream
        audio_stream = yt.streams.filter(only_audio=True).first()
        
        # Download the audio stream
        audio_stream.download(output_path)
        
        print("Audio downloaded successfully!")
    except Exception as e:
        print("Error:", str(e))

# Take input from the user
youtube_url = input("Enter the YouTube audio link: ")
output_path = "./audio"  # Output directory where the audio will be saved

download_audio(youtube_url, output_path)
