import yt_dlp
import whisper
import os

def download_audio(video_url, output_path="audio.mp3"):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    return output_path


def transcribe_with_whisper(video_url):
    try:
        audio_file = download_audio(video_url)

        model = whisper.load_model("tiny")
        result = model.transcribe(audio_file)

        os.remove(audio_file)

        return result["text"]

    except Exception as e:
        print("Whisper error:", e)
        return None