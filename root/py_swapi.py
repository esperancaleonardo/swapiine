#!/usr/bin/python

###
### Leonardo Esperança
###
### python functions to work with
### SWAPI API
###

import swapi

def get_movie(movie_id):
    movie_data = []
    movie = swapi.get_film(movie_id)

    return movie

def movie_to_list(movie):
    movie_list = []

    movie_list.append(movie.title)
    movie_list.append(movie.release_date)
    movie_list.append(movie.director)
    movie_list.append(movie.producer)
    movie_list.append(movie.opening_crawl)

    return movie_list

if __name__ == '__main__':
    for i in range(1,8):
        movie = get_movie(i)
        print (movie_to_list(movie))
