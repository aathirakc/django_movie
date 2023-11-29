from django.http import  HttpResponse
from django.shortcuts import render, redirect
from .models import movie
from .forms import movie_form
# Create your views here.
def home(request):
    context=movie.objects.all()
    obj={
        'obj1':context
    }
    print(obj)

    return render(request,"home.html",obj)

def movie_names(request,id):
    context = movie.objects.get(id=id)
    return render(request,"movie_names.html",{'obj2':context})

def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        details=request.POST.get('details')
        year=request.POST.get('year')
        img=request.FILES['img']
        res=movie(name=name,details=details,year=year,img=img)
        res.save()
        print(name)
    return render(request,"add.html")

def update(request,id):
    movie1=movie.objects.get(id=id)
    form=movie_form(request.POST or None, request.FILES ,instance=movie1)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'form':form,'movie2':movie1})

def delete(request,id):
    movie1=movie.objects.get(id=id)
    movie1.delete()
    return redirect('/')