from django.shortcuts import render
from .models import DemoImage
from .googleVision import googleVision
# Create your views here.
# def index(request):
#     if request.method == 'POST' and request.FILES['deimg']:
#         deimg = request.FILES['deimg']
#         latestImage = DemoImage(dimg = deimg)
#         latestImage.save()
#         image_li_url = googleVision(latestImage.filename())
#         return render(request, 'profane_image/index.html', {'latestImage': latestImage, 'image_li_url': image_li_url })
#     return render(request, 'profane_image/index.html')

def index(request):
    if request.method == 'POST' and request.FILES['deimg']:
        deimg = request.FILES['deimg']
        latestImage = DemoImage(dimg = deimg)
        latestImage.save()
        image_li_url = googleVision(latestImage.filename())
        return render(request, 'profanity_text/Home.html', {'latestImage': latestImage, 'image_li_url': image_li_url })
    return render(request, 'profanity_text/Home.html')