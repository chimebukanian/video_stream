from django.shortcuts import render
from videostreamer.camera import VideoCamera
from django.http.response import StreamingHttpResponse
# Create your views here.
def index(request):
    return render(request, 'videostreamer/index.html')

def feed(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    
def video_stream(request):
    return StreamingHttpResponse(feed(VideoCamera()),
                    content_type='multipart/x-mixed-replace; boundary=frame')