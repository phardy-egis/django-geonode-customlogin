from django.shortcuts import redirect
from urllib.parse import quote_plus


class CheckLoginMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        user = request.user
        if user.is_authenticated:
            # IF a random page is requested by an authenticated user, user is not redirected
            return None
        else:
            # IF login page is requested by a non authenticated user, user is not redirected
            if (
                '/customlogin/' == request.path 
                or '/uploaded'              in request.path
                or '/account/logout'        in request.path
                or '/api/o/v4/tokeninfo'    in request.path
                or '/o/authorize'           in request.path
                or '/o/token'               in request.path
                or '/api/adminRole'         in request.path 
                or '/api/roles'             in request.path 
                or '/api/users'             in request.path 
            ): 
                return None
            # IF another page is requested by a non authenticated user, user is redirected
            else:
                full_path = quote_plus(request.get_full_path())
                return redirect(f'/customlogin?next={full_path}')