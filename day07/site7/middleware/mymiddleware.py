from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse

class MyMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        print("中间件方法 process_request 被调用")
        return None

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("中间件方法 process_view 被调用")
        return None

    def process_response(self, request, response):
        print("中间件方法 process_response 被调用")
        return response

class MyMiddleWare2(MiddlewareMixin):
    def process_request(self, request):
        print("中间件2方法 process_request 被调用")
        return None

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("中间件2方法 process_view 被调用")
        return None

    def process_response(self, request, response):
        print("中间件2方法 process_response 被调用")
        return response

import re

class VisitLimit(MiddlewareMixin):
    visit_times={}

    def process_request(self, request):
        cip = request.META['REMOTE_ADDR']
        # 如果访问的不是/test_middleware，不进行拦截
        if not re.match(r'^/test', request.path_info):
            return
        
        # 获取该IP已访问次数
        times = self.visit_times.get(cip, 0)

        if times >= 5:
            return HttpResponse('You can\'t send GET requests for more than 5 times.')

        self.visit_times[cip] = times + 1
        print("%s has visited %d times" % (cip, times+1))