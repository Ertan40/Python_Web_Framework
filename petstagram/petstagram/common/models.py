from django.contrib.auth import get_user_model
from django.db import models
from petstagram.photos.models import Photo

# common/models.py
UserModel = get_user_model()
class PhotoComment(models.Model):
    MAX_TEXT_LEN = 300
    text = models.CharField(max_length=MAX_TEXT_LEN, null=False, blank=False)
    date_time_of_publication = models.DateTimeField(auto_now_add=True, null=True, blank=False)
    to_photo = models.ForeignKey(Photo, on_delete=models.RESTRICT, null=False, blank=True)
    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT)

    class Meta:
        ordering = ["-date_time_of_publication"]


class PhotoLike(models.Model):
    # photo's field for likes is named '{NAME_OF_THIS_MODEL}_set'
    to_photo = models.ForeignKey(Photo, on_delete=models.RESTRICT, null=False, blank=True)
    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT)
    #when we have users
    #user = models.ForeignKey(User)
