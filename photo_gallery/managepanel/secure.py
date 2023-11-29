import re
from django.shortcuts import redirect
from functools import wraps

ALLOWED_IP_LIST = ["127.0.0.1", "10.*.*.*"]


# IP-based access control.
# 배포 환경에서 안전하지 않음: 변조된 HTTP 헤더를 구분할 수 없음.
# 배포 환경에서는 반드시 신뢰할 수 있는 리버스 프록시에서 X-Forwarded-For 헤더를 통해 발신지를 확인할 것.
def allowed_ips(allowed_ip):
    def decorator(func):
        @wraps(func)
        def inner(request, *args, **kwargs):
            user_ip = request.META['REMOTE_ADDR']
            for ip in allowed_ip:
                if '*' in ip:
                    pattern = re.escape(ip).replace('\\*', '.+')
                    if re.match(pattern, user_ip):
                        return func(request, *args, **kwargs)
                elif user_ip == ip:
                    return func(request, *args, **kwargs)
            return redirect('/error?id=401')
        return inner
    return decorator
