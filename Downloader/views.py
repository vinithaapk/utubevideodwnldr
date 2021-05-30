from django.shortcuts import render
from django.contrib import messages
from pytube import YouTube

def index(request):
    url = request.GET.get('url')
    resolution = request.GET.get('value')
    filename =  request.GET.get('filename')
    messages.info(request,'Welcome')
    try:
        yt_obj = YouTube(url)
        video = yt_obj.streams.get_by_resolution(resolution)
        if video.download(r'D:/MyProjects/Youtube_Video_Downloader/Downloaded_videos', filename = filename):
            messages.success(request,'Video Downloaded Successfully')
    except Exception as e:
        print(e)
    return render(request, 'index.html')




