from django.core.paginator import Paginator
from django.db.models import Q
import requests
from django.shortcuts import redirect, render
from movies.forms import MovieForm
from movies.models import Movies


def movie_list(request):
    object_list = Movies.objects.all()
    paginator = Paginator(object_list, 6)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        
        'page_obj':page_obj
    }
    return render(request,'movie_list.html',context)

def details(request,id):
    result = Movies.objects.get(id = id)
    
    context = {
        'result': result
    }
    return render(request,'details.html',context)

def search(req):
    keyword = req.GET.get('keyword', '')
    print(keyword)
    movies=[]
    movie_count = 0     
    if keyword:
            movies= Movies.objects.filter(Q(title__icontains=keyword))#(Q(description__icontains=keyword) |  Q(product_name__icontains=keyword))
            movie_count =movies.count()
    else:
         movies=Movies.objects.all()
    context = {
        'movies':movies,
        'movie_count':movie_count,
    }

    
    return render(req,'search_list.html',context)

def add_movie(req):
    if req.method == 'POST':
        title = req.POST.get('title',)
        name = req.POST.get('name',)
        summary = req.POST.get('summary',)
        release_year = req.POST.get('release_year',)
        rating = req.POST.get('rating',)
        image = req.FILES['image']
        
        movie = Movies(genre=name,title=title,summary=summary,release_year=release_year,rating=rating,title_image=image)
        
        movie.save()
        return redirect('/')
    return render(req,'add.html')

def delete(req,id):
    if req.method == 'POST':
        movie = Movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(req,'delete.html')

def update(req,id):
    result = Movies.objects.get(id=id)
    form = MovieForm(req.POST or None, req.FILES,instance=result)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(req,'edit.html',{'form':form,'result':result})