from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from movies.forms import MovieForm

# Create your views here.
from movies.models import Movie, apiMovies
import requests
from django.shortcuts import render

# myapp/views.py
import requests
from django.shortcuts import render
from django.db.models import Q

def fetch_data(request):
    url = "https://imdb8.p.rapidapi.com/v2/search"
    querystring = {"searchTerm": "game", "type": "NAME", "first": "10"}

    headers = {
        "x-rapidapi-key": "9da9b05cb6msh36b46c773430828p12266ajsn89915f9bdc25",
        "x-rapidapi-host": "imdb8.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json().get('data', {}).get('mainSearch', {}).get('edges', [])
    
    results = []
    for edge in data:
        node = edge.get('node', {}).get('entity', {})
        name_text = node.get('nameText', {}).get('text', '')

        known_for = node.get('knownFor', {}).get('edges', [])
        for kf_edge in known_for:
            kf_node = kf_edge.get('node', {})
            title_text = kf_node.get('title', {}).get('titleText', {}).get('text', '')
            # id = kf_node.get('title', {}).get('title', {}).get('id', '')
            release_year = kf_node.get('title', {}).get('releaseYear', {}).get('year', '')
            release_date = kf_node.get('title', {}).get('releaseDate', {}).get('day', '')
            release_month = kf_node.get('title', {}).get('releaseDate', {}).get('month', '')
            rating = kf_node.get('title', {}).get('ratingsSummary', {}).get('aggregateRating', '')
            title_image_url = kf_node.get('title', {}).get('primaryImage', {}).get('url', '')
            # print(rating,'------------------------->>>')
            item, created = apiMovies.objects.update_or_create(
                name=name_text,
                title=title_text,
                defaults={
                    'release_date': release_date,
                    'release_month': release_month,
                    'release_year': release_year,
                    'rating': rating,
                    'title_image_url': title_image_url,
                }
            )
            results.append(item)
    object_list = apiMovies.objects.all()
    paginator = Paginator(object_list, 6)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'results': results,
        'page_obj':page_obj
    }
    
    return render(request, 'movie_list.html', context)


# def movie_list(request):
#     movies = Movie.objects.all()
#     return render(request,'movie_list.html', {'movies': movies})

def details(request,id):
    result = apiMovies.objects.get(id = id)
    
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
            movies= apiMovies.objects.filter(Q(title__icontains=keyword))#(Q(description__icontains=keyword) |  Q(product_name__icontains=keyword))
            movie_count =movies.count()
    else:
         movies=apiMovies.objects.all()
    context = {
        'movies':movies,
        'movie_count':movie_count,
    }

    
    return render(req,'search_list.html',context)

# def add_movie(req):
#     if req.method == 'POST':
#         title = req.POST.get('title',)
#         director = req.POST.get('director',)
#         genre = req.POST.get('genre',)
#         summary = req.POST.get('summary',)

#         image = req.FILES['image']
#         release_year = req.POST.get('release_year',)

#         movie = Movie(title=title,director=director,genre=genre,summary=summary,image=image,release_year=release_year)
#         movie.save()
        
#     return render(req,'add.html')

# def update(req,id):
#     result = apiMovies.objects.get(id=id)
#     form = MovieForm(req.POST or None, req.FILES,instance=result)
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#     return render(req,'edit.html',{'form':form,'result':result})
# def delete(req,id):
#     if req.method == 'POST':
#         movie = apiMovies.objects.get(id=id)
#         movie.delete()
#         return redirect('/')
#     return render(req,'delete.html')