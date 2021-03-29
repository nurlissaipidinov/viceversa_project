from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return HttpResponse("This is about page")


def home(request):
    return render(
        request, 'home.html'
    )


def reverse(request):
    user_text = request.GET['usertext']
    reversed_text = user_text[::-1]
    return render(
        request, 'reverse.html', {'usertext': user_text,
                                  'reversedtext': reversed_text}
    )
