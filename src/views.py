
from django.shortcuts import render
from newsletter.forms import SearchLocationForm, GitSearchForm




def about(request):
    return render(request, "about.html", {})

def thanks(request):
    return render(request, "thankyou.html", {})

def blog(request):
    return render(request, "blog.html", {})

def gpsSearch(request):
    title = "GPS Coordinates lookup"
    form = SearchLocationForm(request.POST or None)
    location =[]
    city_name = ""

    if form.is_valid():
        # form.save()
        instance = form.save(commit=False)

        city_name = form.cleaned_data.get("city_name")
        if not city_name:
            city_name = "New city name"
        instance.city_name = city_name
        # if not instance.full_name:
        #     instance.full_name = "James"
        instance.save()

        location = form.search(city_name)


    context = {
        "form": form,
        "title": title,
        "location": location,
        "city_name": city_name,
    }

    return render(request, "forms.html", context)

def gitSearch(request):
    title = "GitHub User Search"
    form = GitSearchForm(request.POST or None)
    user_name = ""
    followers = ""
    image = ""

    context = {
    "form": form,
    "title": title,
    }

    if form.is_valid():

        instance = form.save(commit=False)

        user_name = form.cleaned_data.get("user_name")
        if not user_name:
            user_name = "New user name"
        instance.user_name = user_name

        instance.save()

        followers = form.gitSearch(user_name)

        context = {
        "form": form,
        "title": title,
        "user_name": user_name,
        "followers": followers[1],
        "image": followers[0],
        }

    return render(request, "gitsearch.html", context)
