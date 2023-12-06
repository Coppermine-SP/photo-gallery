from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from photo_gallery.models import photo_metadata


# Create your views here.
def list_view(request):
    content_per_page = 10
    categories = ["landscape", "portrait", "innovation"]
    friendly_name = {"landscape" : "Landscapes", "portrait" : "Portraits", "innovation" : "Innovations"}
    category = request.GET.get("category", "NONE")
    page = int(request.GET.get("page", "1"))

    if category == "NONE":
        return redirect("/error?id=404")
    photo_list = photo_metadata.objects.filter(category=category).order_by("id")
    pages = len(photo_list) // content_per_page + 1

    if page > pages:
        return redirect("/error?id=400")

    paginator = Paginator(photo_list, content_per_page)
    photos = paginator.get_page(page)

    if page == 1:
        prev_page_url = "None"
    else:
        prev_page_url = f"/list?category={category}&page={page-1}"

    if page >= pages:
        next_page_url = "None"
    else:
        next_page_url = f"/list?category={category}&page={page + 1}"

    return render(request, "list/list.html", {"photos": photos,
                                              "count": len(photo_list),
                                              "collection": friendly_name[category],
                                              "current_page": page,
                                              "pages": pages,
                                              "next_page_url": next_page_url,
                                              "prev_page_url": prev_page_url
                                              })