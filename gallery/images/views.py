from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import images, albums


@login_required(login_url = 'login')
def hub(request):
    image_for_gallery = images.objects.all()
    owner = request.user
    album_names = albums.objects.filter(owner = owner)
    album = request.GET.get('album')
    
    if album != None:
        image_for_gallery = images.objects.filter(album__album_name=album, album__owner=owner)
    else:
        image_for_gallery = images.objects.filter(album__owner=owner)

    all_albums = {'image_for_gallery': image_for_gallery, 'album_names': album_names}
    return render(request, 'images/hub.html', all_albums)

def registerUsers(request):
    userForm = UserCreationForm()
    cur_type = 'reg'
    if request.method == "POST":
        userForm = UserCreationForm(request.POST)

        # problem with unamed attribute was solved using this code: https://stackoverflow.com/questions/29594330/usercreationform-object-has-no-attribute-get-username-django-1-8

        if userForm.is_valid():
            userForm.save()
            user = userForm.cleaned_data['username']
            password = userForm.cleaned_data['password1']
            indv_user = authenticate(request, username=user, password=password)

            if indv_user is not None:
                login(request, indv_user)
                return redirect('hub')

    return render(request, 'images/login.html', {'userForm': userForm, 'cur_type': cur_type})

@login_required(login_url = 'login')
def logoutUsers(request):
    logout(request)
    return redirect('login')
    
def loginUsers(request):
    if request.method == "POST":
        password = request.POST['password']
        user = request.POST['user']
        indv_user = authenticate(request, username=user, password=password)

        if indv_user is not None:

            login(request, indv_user)
            return redirect('hub')

    return render(request, 'images/login.html')

@login_required(login_url = 'login')
def upload_image(request):
    owner = request.user
    if request.method == 'POST':
        img = request.FILES.get("img")
        formFields = request.POST

        if formFields['new_album'] != "":
            album, created = albums.objects.get_or_create(album_name = formFields["new_album"], owner = owner)
        else:
            album = albums.objects.get(id = formFields['album'])
        
        image = images.objects.create(album = album, caption = formFields["caption"], gallery_image = img)

    album_names = albums.objects.filter(owner=owner) 
    return render(request, 'images/upload_image.html',  {'album_names': album_names})

@login_required(login_url = 'login')
def view_image(request, primary):
    image_to_view = images.objects.get(id=primary)
    view = {'image_to_view': image_to_view}
    return render(request, 'images/view_image.html', view)

