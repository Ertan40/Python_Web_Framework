
def is_owner(request, obj):
    return request.user == obj.user


# class OwnerRequired:
#
#     def get(self, request, *args, **kwargs):
#         result = super().get(request, *args, **kwargs)
#
#         if request.user == self.object.user:
#             return result
#         else:
#             return '...'
#     def post(....)

# import functools
#
#
# def owner_required(view_func):
#     functools.wraps(view_func)
#
#     def wrapper(*args, **kwargs):
#         return view_func(*args, **kwargs)
#
#     return wrapper
