from pytube import YouTube

def videoDownload(url):
    try:
        youtube = YouTube(url)
        stream = youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if not stream:
            raise ValueError("Downloadble stream was not found.") # Downloadble stream was not found.
        
        print(f"Downloading: {youtube.title}...")
        stream.download()
        print("Downloaded Successfully.")
    
    except Exception as e:
        print(f"An ERROR occured: {e}")

def main():
    try:
        url = input("URL: ").strip()
        videoDownload(url)
    
    except KeyboardInterrupt:
        print("\n\nStopping...")
    
    except Exception as e:
        print(f"Unexpected ERROR: {e}")

if __name__ == "__main__":
    main()
