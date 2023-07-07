from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from petstagram.pets.models import Pet
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm, PhotoDeleteForm
from petstagram.photos.models import Photo

@login_required
def add_photo(request):
    if request.method == 'GET':
        form = PhotoCreateForm()
    else:
        form = PhotoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            form.save_m2m()
            return redirect('details photo', pk=photo.pk)

    context = {
        'form': form,
    }
    return render(request, 'photos/photo-add-page.html', context)


def edit_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = PhotoEditForm(instance=photo)
    else:
        form = PhotoEditForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('details photo', pk=pk)

    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'photos/photo-edit-page.html', context)


def details_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    # likes = photo.photolike_set.count()  # or likes = PhotoLike.objects.filter(to_photo_id=pk)
    likes = Photo.objects.filter(pk=pk, user_id=request.user.pk)
    comments = photo.photocomment_set.all()
    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
        'is_owner': request.user == photo.user,
    }
    return render(request, 'photos/photo-details-page.html', context)


def delete_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = PhotoDeleteForm(instance=photo)
    else:
        form = PhotoDeleteForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, template_name='photos/photo-delete-page.html', context=context)



# def get_post_photo_form(request, form, success_url, template_path, pk=None):
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect(success_url)
#     context = {'form': form, 'pk': pk}
#     return render(request, template_path, context)
#
#
# def add_photo(request):
#     return get_post_photo_form(request, PhotoCreateForm(request.POST or None),
#                                success_url=reverse('details_photo'), kwargs={'pk': photo.pk})

# def edit_photo(request, pk):
#     photo = Photo.objects.filter(pk=pk).get()
#     return get_post_photo_form(request, PhotoEditForm(request.POST or None),
#                                success_url=reverse('index'), template_path='photos/photo-edit-page.html', pk=pk)

# def delete_photo(request, pk):
#     photo = Photo.objects.filter(pk=pk).get()
#     return get_post_photo_form(request, PhotoDeleteForm(request.POST or None),
#                                success_url=reverse('index'), template_path='photos/photo-delete-page.html', pk=pk)
