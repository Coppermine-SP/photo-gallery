from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'mainpage/index.html')


def contributors(request):
    return render(request, 'mainpage/contributors.html')

def about(request):
    return render(request, 'mainpage/about.html')

def error(request, errid=0):
    errList = {'404': "요청한 페이지 또는 자료를 찾을 수 없습니다.", '500': "서버에 내부 오류가 있습니다.", '401': "귀하는 이 페이지를 볼 권한 또는 자격이 없습니다.",
               '400': "잘못 된 요청입니다."}

    if errid == 0:
        errid = request.GET.get('id')

    if errid is None:
        errstr = "알 수 없는 오류."
    else:
        if errid not in errList.keys():
            errstr = "알 수 없는 오류."
        else:
            errstr = f"{errid}: {errList[errid]}"

    return render(request, 'mainpage/error.html', {'errstr': errstr})
