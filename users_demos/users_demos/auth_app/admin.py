# from django.contrib import admin
#
# from django.contrib.auth import admin as auth_admin, get_user_model
#
# # Register your models here.
# UserModel = get_user_model()
#
#
# @admin.register(UserModel)
# class AppUserAdmin(auth_admin.UserAdmin):
#     ordering = ('email',)
#     list_display = ['e-mail', 'date_joined', 'last_login']
#     list_filter = ()
#     add_form = SignUpForm
#       add_field_sets = (
#           (
#               None,
#               {
#                   'classes': ('wide',),
#                   'fields': ('email', 'password1', 'password2'),
#               }
#           ),
#           (
#               None,
#               {
#                   'classes': ('wide',),
#                   'fields': ('first_name', 'last_name', 'age'),
#               }
#           ),
#       )