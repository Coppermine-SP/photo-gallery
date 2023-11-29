import re
from django.shortcuts import redirect
from functools import wraps

ALLOWED_IP_LIST = ["127.0.0.1", "10.*.*.*"]


# IP-based access control.
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
