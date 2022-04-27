from django.db import models
from django.contrib.auth.models import User

class albums(models.Model):
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    album_name = models.CharField(max_length = 100, blank = False, null = False)

    def __str__(self):
        return self.album_name


class images(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    gallery_image = models.ImageField(blank = False, null = False)
    album = models.ForeignKey(albums,blank = True, null=True, on_delete=models.SET_NULL)
    caption = models.CharField(max_length = 50, blank = False,null = False)

    def __str__(self):
        return self.caption


