from django.shortcuts import render

def hub(request):
    return render(request, 'images/hub.html')

def view_image(request, primary):
    return render(request, 'images/view_image.html')

def upload_image(request):
    return render(request, 'images/upload_image.html')

