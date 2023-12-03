from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from photo_gallery.models import photo_metadata


# Create your views here.
def view(request):
    target_id = request.GET.get("id")
    if target_id is None:
        return redirect("/error?id=400")
    try:
        target = photo_metadata.objects.get(id=target_id)
        return render(request, "view/view.html", {"target": target})
    except photo_metadata.DoesNotExist:
        return redirect("/error?id=404")
    except:
        return redirect("/error?id=500")

