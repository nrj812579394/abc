from django.shortcuts import render, HttpResponseRedirect

from backweb.models import Article





def share(request):
    if request.method == 'GET':
        return render(request, 'web/share.html')


def my_index(request):
    if request.method == 'GET':
        arts = Article.objects.all()
        return render(request, 'web/index.html', {'arts': arts})