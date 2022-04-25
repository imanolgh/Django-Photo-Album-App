from django.shortcuts import render
from .models import images, albums

def hub(request):
    image_for_gallery = images.objects.all()
    album_names = albums.objects.all()
    all_albums = {'image_for_gallery': image_for_gallery, 'album_names': album_names}
    return render(request, 'images/hub.html', all_albums)

def upload_image(request):
    album_names = albums.objects.all() 
    return render(request, 'images/upload_image.html',  {'album_names': album_names})

def view_image(request, primary):
    image_to_view = images.objects.get(id=primary)
    view = {'image_to_view': image_to_view}
    return render(request, 'images/view_image.html', view)

