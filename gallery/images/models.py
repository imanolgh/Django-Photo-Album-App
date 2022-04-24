from django.db import models

class albums(models.Model):
    album_name = models.CharField(max_length = 100, blank = False, null = False)

    def __str__(self):
        return self.album_name


class images(models.Model):
    gallery_image = models.ImageField(blank = False, null = False)
    album = models.ForeignKey(albums,blank = True, null=True, on_delete=models.SET_NULL)
    caption = models.CharField(max_length = 50, blank = False,null = False)

    def __str__(self):
        return self.caption


