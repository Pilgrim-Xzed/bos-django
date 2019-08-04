from django.shortcuts import render, HttpResponse
from .models import Setting, Document, Work, Publication
# Create your views here.

def index(request):
    settings = Setting.objects.get(category_id="2")
    documents =Document.objects.all().order_by('-id')[:3]
    works = Work.objects.all()
    context={
        "settings":settings,
        "documents":documents,
        "works":works
    }
    return render(request,'home.html',context)


def documents(request):
    documents =Document.objects.all()
    settings = Setting.objects.get(category_id="2")
    args = {
        "documents":documents,
        "settings":settings,
    }

    return render(request,'documents.html',args)


def works(request):
    settings = Setting.objects.get(category_id="2")
    works = Work.objects.all()
    context = {
        "works":works,
        "settings":settings
    }

    return render(request,'works.html',context)


def publications(request):
     settings = Setting.objects.get(category_id="2")
     publications = Publication.objects.all()
     context = {
         "settings":settings,
         "publications":publications
     }

     return render(request,'publications.html',context)