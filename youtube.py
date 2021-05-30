from pytube import YouTube
youtube_video_url = 'https://www.youtube.com/watch?v=Yf9Nlq5wrf8'
try:
    yt_obj = YouTube(youtube_video_url)
    resolution = input("Enter resolution : ")
    video = yt_obj.streams.get_by_resolution(resolution+'p')
    video.download(r'D:\My Projects\Youtube Video Downloader\Downloaded_videos')
    print('Video Downloaded Successfully')
except Exception as e:
    print(e)
