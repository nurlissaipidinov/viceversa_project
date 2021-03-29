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
    words = user_text.split()
    len_of_words = len(words)
    return render(
        request, 'reverse.html', {'usertext': user_text,
                                  'reversedtext': reversed_text,
                                  'len_of_words': len_of_words
                                  }
    )
