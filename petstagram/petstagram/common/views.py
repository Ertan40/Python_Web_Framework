import pyperclip
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from petstagram.common.forms import PhotoCommentForm, SearchPhotosForm
from petstagram.common.models import PhotoLike
from petstagram.common.utils import get_photo_url, apply_likes_count, apply_user_liked_photo
from petstagram.photos.models import Photo

def index(request):
    search_form = SearchPhotosForm(request.GET)
    search_pattern = None

    if search_form.is_valid():
        search_pattern = search_form.cleaned_data['pet_name']

    photos = Photo.objects.all()

    if search_pattern:
        photos = photos.filter(tagged_pets__name__icontains=search_pattern)


    photos = [apply_likes_count(photo) for photo in Photo.objects.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]


    context = {
        'photos': photos,
        'comment_form': PhotoCommentForm(),
        'search_form': search_form,
    }
    return render(request, 'common/home-page.html', context)
# def get_user_liked_photos(photo_id):  moved to utils.py
#     return PhotoLike.objects.filter(to_photo_id=photo_id)

@login_required
def like_photo(request, photo_id):
    # without get() becasue if there are no likes it will crash
    user_liked_photos = PhotoLike.objects.filter(to_photo_id=photo_id, user_id=request.user.pk)
    if user_liked_photos:
        user_liked_photos.delete()
    else:
        # Variant 1
        PhotoLike.objects.create(to_photo_id=photo_id, user_id=request.user.pk)
    # redirect_path = request.META['HTTP_REFERER'] + f'#photo-{photo_id}' moved to utils.py
    # http://127.0.0.1:8000/#photo-1
    return redirect(get_photo_url(request, photo_id))
    # Variant 2
    # photo_like = PhotoLike(photo_id=photo_id)
    # photo_like.save()

def share_photo(request, photo_id):
    photo_details_url = reverse('details photo', kwargs={'pk': photo_id})
    pyperclip.copy(f'http://127.0.0.1:8000{photo_details_url}')
    return redirect(get_photo_url(request, photo_id))  # was repeating therefore placed to utils.py

@login_required
def comment_photo(request, photo_id):
    photo = Photo.objects.filter(pk=photo_id).get()
    form = PhotoCommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.to_photo = photo
        comment.save()
        # photo.comment_set.add(comment)
        # photo.save()

    return redirect("index")
