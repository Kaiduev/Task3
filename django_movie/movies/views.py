from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .models import Movie,Actor
from django.views.generic.base import View

from .forms import ReviewFrom


class MoviesView(ListView):

    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/movie_list.html"


class MovieDetailsView(DetailView):

    model = Movie
    slug_field = "url"


class AddReview(View):

    def post(self, request,pk):
        form = ReviewFrom(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())