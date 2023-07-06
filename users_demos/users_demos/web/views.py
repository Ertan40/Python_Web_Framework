from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import mixins as auto_mixins
from django.views import generic as views
from django.contrib.auth.models import User
from django.shortcuts import render

from users_demos.auth_app.models import AppUser


# Create your views here.
class UsersListView(auto_mixins.LoginRequiredMixin, views.ListView):
    model = User
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        # context['has_email'] = AppUser.has_email(self.request.user)
        print(self.request.user.__class__)
        return context

# AUTH_USER_MODEL = 'auth_app.AppUser'
# after migrating the new models then we have to modify the model :
# from django.contrib.auth import mixins as auto_mixins, get_user_model
# UserModel = get_user_model()
# model = UserModel
