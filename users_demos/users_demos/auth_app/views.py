from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import forms as auth_forms, authenticate, login
from django.contrib.auth import forms as auth_forms, views as auth_views
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

# password: D@123mkp

# UserModel = get_user_model()
class SignUpForm(auth_forms.UserCreationForm):
    # first_name = forms.CharField()
    # last_name = forms.CharField()
    # age = forms.IntegerField()

    class Meta:
        model = User
        # model = UserModel
        fields = ('first_name', 'last_name', 'username')
        # fields = (UserModel.USERNAME_FIELD, 'password1', 'password2', 'first_name', 'last_name', 'age')
        field_classes = {'username': auth_forms.UsernameField}

    # save with data for  profile
    # def save(self, commit=True):
    #     user = super().save(commit=commit)
    #     profile = Profile(
    #     first_name = self.cleaned_data['first_name'],
    #     last_name = self.cleaned_data['last_name'],
    #     age = self.cleaned_data['age'],
    #     user=user)
    #     if commit:
    #         profile.save()
    #     return user

    # save with empty profile
    # def save(self, commit=True):
    #     user = super().save(commit=commit)
    #     profile = Profile(user=user)
    #     if commit:
    #         profile.save()

    #how to generate username dynamically - for demo purposes
    # def save(self, commit=True):
    #     user = super().save(commit=commit)
    #     user.username = user.first_name + '-' + user.last_name
    #     if commit:
    #         user.save()
    #     return user


class SignUpView(views.CreateView):
    template_name = 'sign-up.html'
    form_class = SignUpForm       # open-closed extension
    # success_url = reverse_lazy('sign up')
    success_url = reverse_lazy('index')

    # Signs the user in , after successful sign up
    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class SignInView(auth_views.LoginView):
    template_name = 'sign-in.html'
    success_url = reverse_lazy('index')
    # def get_success_url(self):
    #     if self.success_url:
    #         return self.success_url
    #
    #     return self.get_redirect_url() or self.get_default_redirect_url()
    # can be done also as below:
    # <input name="next" type="hidden" value="{{ next }}"> in sign-in.html
class SignOutView(auth_views.LogoutView):
    template_name = 'sign-out.html'
    # success_url = reverse_lazy('index')


# class SignInForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField()
#
# def sign_in(request):
#     if request.method == 'GET':
#         form = SignInForm()
#
#     else:
#         form = SignInForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             # user = authenticate(request, username=username, password=password)
#             user = authenticate(request, **form.cleaned_data)
#             # print(user)
#
#             if user:
#                 login(request, user)
#
#     context = {'form': form}
#     return render(request, 'sign-in.html', context)

# easier way to implement instead of upper version with built-in:
# in auth_app\urls.py
# path('sign-in/', LoginView.as_view(template_name='sign-in.html'), name='sign in'),
# but not a good practise and better to have ours

# AUTH_USER_MODEL = 'auth_app.AppUser'
# after migrating the new models then we have to modify the model :
# from django.contrib.auth import mixins as auto_mixins, get_user_model
# UserModel = get_user_model()
# model = UserModel

