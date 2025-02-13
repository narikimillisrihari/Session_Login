from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import JsonResponse

class AutoLogoutMiddleware(MiddlewareMixin):
    def process_request(self,request):
        if request.user.is_authenticated:
            if not request.session.get('userid'):
                logout(request)
            return JsonResponse({"error":"session expried. Please log in again"})
        
