from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Hello, world. January challenges."
    elif month == "february":
        challenge_text = "Hello, world.February Challenge."
    elif month == "march":
        challenge_text = "Hello, world.March Challenge."
    elif month == "april":
        challenge_text = "Hello, world.April Challenge."
    elif month == "may":
        challenge_text = "Hello, world.May Challenge."
    elif month == "june":
        challenge_text = "Hello, world.June Challenge."
    elif month == "july":
        challenge_text = "Hello, world.July Challenge."
    elif month == "august":
        challenge_text = "Hello, world.August Challenge."
    elif month == "september":
        challenge_text = "Hello, world.September Challenge."
    elif month == "october":
        challenge_text = "Hello, world.October Challenge."
    elif month == "november":
        challenge_text = "Hello, world.November Challenge."
    elif month == "december":
        challenge_text = "Hello, world.December Challenge."
    else:
        return HttpResponseNotFound("This month is not supported.")
    return HttpResponse(challenge_text)
