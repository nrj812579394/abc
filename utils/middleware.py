from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect
from backweb.models import MyUser


class LoginStatusMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 在访问登陆和注册的时候，不需要做以下的登陆校验功能
        if request.path in ['/backweb/login/', '/backweb/register/']:
            return None
        # 登陆校验
        user_id = request.session.get('user_id')
        if user_id:
            user = MyUser.objects.get(pk=user_id)
            request.user = user
        else:
            return HttpResponseRedirect('/backweb/login/')

    def procsrr_response(self, request, response):

        return response
