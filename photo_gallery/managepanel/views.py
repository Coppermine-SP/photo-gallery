from django.shortcuts import render
from django.http import HttpResponse
from .secure import *


@allowed_ips(ALLOWED_IP_LIST)
def manage(request):
    return HttpResponse("Hello, World!")