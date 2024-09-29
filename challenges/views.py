from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse

monthly_challenges = {
    "january": "start of the year",
    "february": "not too late!",
    "march": "oops, it's march now!",
    "april": "April fools!",
    "may": "Almost half way!",
    "june": "Finally half left",
    "july": "Summer starts now",
    "august": "Birthday month! yay!",
    "september": "Labor day long weekend",
    "october": "Germany!!!",
    "november": "Getting cold in New York",
    "december": None
}

# Create your views here.
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid Month</h1>")
    
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
    

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month})
    except:
        raise Http404()
    
    
# def index(request):
#     months = list(monthly_challenges.keys())
#     response_data = "<h1><ul>"
#     for month in months:
#         capitalized_month = month.capitalize()
#         redirect_path = reverse("month-challenge", args=[month])
#         response_data += f"<li><a href=\"{redirect_path}\">{capitalized_month}</a></li>"
#     response_data += "</ul></h1>"
#     return HttpResponse(response_data)


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })
    
    