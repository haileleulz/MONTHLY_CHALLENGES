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
    "december": "Hello, world.December Challenge.",
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalize_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\'{month_path}\'>{capitalize_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

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
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except KeyError:
        return HttpResponseNotFound("<h1>This month is not supported.</h1>")
    # except KeyError:
    #     return HttpResponse("<h1>This month is not supported.</h1>", status=404)
    # except KeyError:
    #     response = HttpResponseNotFound("<h1>This month is not supported.</h1>")
    #     print(response.status_code)
    #     print(response["Content-Type"])
    #     return response

# except KeyError:
#     response = HttpResponseNotFound("<h1>This month is not supported.</h1>")
#     print(response.status_code)
#     print(response["Content-Type"])
#     return response