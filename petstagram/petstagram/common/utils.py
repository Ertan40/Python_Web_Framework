from petstagram.common.models import PhotoLike

# deleted after user was created
# def get_user_liked_photos(photo_id):
#     return PhotoLike.objects.filter(to_photo_id=photo_id)


def get_photo_url(request, photo_id):
    return request.META['HTTP_REFERER'] + f'#photo-{photo_id}'


def apply_likes_count(photo):
    # photo's field for likes is named '{NAME_OF_THIS_MODEL}_set' # placed from common/views
    photo.likes_count = photo.photolike_set.count()
    return photo

def apply_user_liked_photo(photo):
    #TODO : fix for current user when authentication is available
    photo.is_liked_by_user = photo.likes_count > 0
    return photo