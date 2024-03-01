from pytube import YouTube


def download_youtube_video(url, save_path="./"):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        print(f"Downloading: {yt.title}")
        stream.download(output_path=save_path)
        print("Download completed successfully!")
    except Exception as e:
        print(f"Error downloading video: {e}")


if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_youtube_video(video_url)
