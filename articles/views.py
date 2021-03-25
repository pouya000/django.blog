from django.shortcuts import render
from . import models

def article_list (request):
    arc = models.Articles.objects.all().order_by('date')
    arg={'artic': arc}
    return render(request,'articles/articlelist.html',arg)

