from django.shortcuts import render

from django.contrib.auth import views as auth_views, get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.accounts.forms import UserCreateForm

# def login_user(request):
#     return render(request, 'accounts/login-page.html')
# always get the 'user model' with get_user_model
UserModel = get_user_model()

class SignInView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    # success_url = ''
    # def get_success_url(self):


# def register_user(request):
#     return render(request, 'accounts/register-page.html')
class SignUpView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')


class SignOutView(auth_views.LogoutView):
    ...
    # next_page = reverse_lazy('index')

# def details_user(request, pk):
#     return render(request, 'accounts/profile-details-page.html')
class UserDetailsView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        context['pets_count'] = self.object.pet_set.count()
        context['photos_count'] = self.object.photo_set.count()
        # photos = self.object.photo_set.all()
        photos = self.object.photo_set.prefetch_related('photolike_set')
        # .select_related('user')  # if need user
        # N + 1 query problem
        context['likes_count'] = sum(x.photolike_set.count() for x in photos)
        return context

# def edit_user(request, pk):
#     return render(request, 'accounts/profile-edit-page.html')

class UserEditView(views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'email', 'gender')

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })

# def delete_user(request, pk):
#     return render(request, 'accounts/profile-delete-page.html')

class UserDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')





