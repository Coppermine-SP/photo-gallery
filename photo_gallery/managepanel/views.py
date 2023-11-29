import re
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from functools import wraps

# IP-based access control.
ALLOWED_IP_LIST = ["127.0.0.1", "10.*.*.*"]
def allowed_ips(allowed_ips):
    def decorator(func):
        @wraps(func)
        def inner(request, *args, **kwargs):
            user_ip = request.META['REMOTE_ADDR']
            for ip in allowed_ips:
                # 와일드카드 처리
                if '*' in ip:
                    pattern = re.escape(ip).replace('\\*', '.+')
                    if re.match(pattern, user_ip):
                        return func(request, *args, **kwargs)
                # 정확한 IP 주소 비교
                elif user_ip == ip:
                    return func(request, *args, **kwargs)
            return redirect('/error?id=401')
        return inner
    return decorator

@allowed_ips(ALLOWED_IP_LIST)
def manage(request):
    return HttpResponse("Hello, World!")