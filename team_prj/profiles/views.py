from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def signup(request):
    if request.method == "POST":
        userform = UserCreationForm(request.POST)
        if userform.is_valid():
            userform.save()

            return HttpResponseRedirect(
                reverse("signup_ok")
            )

    elif request.method == "GET":
        userform = UserCreationForm()

    return render(request, "signup.html", {
        "userform": userform,
    })
