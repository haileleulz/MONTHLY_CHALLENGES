from calendar import month

from django.shortcuts import render
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
)

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
    "december": "Hello, world.December Challenge.",
}

# Create your views here.


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("This month is not supported.")

    forward_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + forward_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except KeyError:
        return HttpResponseNotFound("This month is not supported.")
