from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_sameorigin
from .secure import *
from photo_gallery.models import photo_metadata


@allowed_ips(ALLOWED_IP_LIST)
def manage(request):
    cat = request.GET.get("category", "*")
    if cat == "*":
        photo_list = photo_metadata.objects.all()
    elif cat in ["landscape", "portrait", "innovation"]:
        photo_list = photo_metadata.objects.filter(category=cat)
    else:
        return redirect("/error?id=404")
    return render(request, "managepanel/manage.html", {"photoList": photo_list, "category" : cat, "rowCount" : len(photo_list), "ip" : request.META.get("REMOTE_ADDR"), "user_agent" : request.META.get("HTTP_USER_AGENT"), "is_secure" : request.is_secure()})


@allowed_ips(ALLOWED_IP_LIST)
@xframe_options_sameorigin
def upload(request):
    if request.method == 'POST':
        image = request.FILES['image']
        description = request.POST.get('description')
        category = request.POST.get('category')
        photo_metadata.objects.create(image=image, description=description, category=category)
        return render(request, "managepanel/success.html")
    else:
        if "HTTP_REFERER" in request.META:
            referer = request.META["HTTP_REFERER"]
            if '/manage' in referer:
                return render(request, "managepanel/upload.html")
            else:
                return redirect("/error?id=400")
        return redirect("/error?id=400")


@allowed_ips(ALLOWED_IP_LIST)
def delete(request):
    if request.method != 'POST':
        return redirect("/error?id=400")
    else:
        target_id = request.POST.get('id')
        try:
            target = photo_metadata.objects.get(id=target_id)
            target.delete()
        except Exception as e:
            print(e)
            return HttpResponse(status=500)
        return HttpResponse()
