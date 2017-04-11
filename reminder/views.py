from django.shortcuts import render

from django.http import HttpResponse


def manage(request):
    zipcodes = range(10001, 10010)
    return render(request, 'manage.html', {'zipcodes': zipcodes})

