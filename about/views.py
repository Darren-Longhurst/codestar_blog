from django.shortcuts import render
from .models import about

# Create your views here.

def about_me(request):
    """
    Display the About page.

    **Context**

    ``about``
        An instance of :model:`about.about`.

    **Template:**

    :template:`about/about.html`
    """

    about_me = about.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about,},
    )