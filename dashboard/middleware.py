from django.urls import resolve
from django.contrib.auth.decorators import login_required


class ProtectPathMiddleware:
  def __init__(self, get_response):
    self.get_response = get_response

  def __call__(self, request):
    unprotected_routes = ['login', 'register', 'logout']
    current_route = resolve(request.path_info).url_name

    if current_route not in unprotected_routes and not request.user.is_authenticated:
      return login_required(current_route)(request)

    return self.get_response(request)
