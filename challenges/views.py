from calendar import month
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "january": "Hello, world. January challenges.",
    "february": "Hello, world.February Challenge.",
    "march": "Hello, world.March Challenge.",
    "april": "Hello, world.April Challenge.",
    "may": "Hello, world.May Challenge.",
    "june": "Hello, world.June Challenge.",
    "july": "Hello, world.July Challenge.",
    "august": "Hello, world.August Challenge.",
    "september": "Hello, world.September Challenge.",
    "october": "Hello, world.October Challenge.",
    "november": "Hello, world.November Challenge.",
    "december": None,
}

# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {"months": months})


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>This month is not supported.</h1>")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(
            request,
            "challenges/challenge.html",
            {"text": challenge_text, "month_name": month},
        )
    except:
        return HttpResponseNotFound("<h1>This month is not supported.</h1>")
