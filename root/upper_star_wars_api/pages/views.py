from django.shortcuts import render, HttpResponse
import swapi
from time import sleep
from operator import itemgetter
# Create your views here.

""" homepage view definition, returns a rendered .html file """
def homepage_view(request, *args, **kwargs):
    #return HttpResponse("<h1>HomePage</h1><br/><h3>Welcome</h3></br>List of SW Movies:</br>Episode 1 - The Phantom Menace</br>Episode 2 - Attack Of The Clones</br>Episode 3 - Revenge Of The Sith</br>Episode 4 - A New Hope</br>Episode 5 - The Empire Strikes Back</br>Episode 6 - Return Of The Jedi</br>Episode 7 - The Force Awakens")
    dict = get_movies_list_by_ep()
    return render(request, "index_data.html", dict)

""" movie view definition, returns a rendered .html
    file with aditional information in dict dictionary """
def ep1_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Episode 1 - The Phantom Menace</h1>")
    dict = gen_dict_from_movie(4)
    return render(request, "episode1.html", dict)

""" movie view definition, returns a rendered .html
    file with aditional information in dict dictionary """
def ep2_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Episode 2 - Attack Of The Clones</h1>")
    dict = gen_dict_from_movie(5)
    return render(request, "episode2.html", dict)

""" movie view definition, returns a rendered .html
    file with aditional information in dict dictionary """
def ep3_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Episode 3 - Revenge Of The Sith</h1>")
    dict = gen_dict_from_movie(6)
    return render(request, "episode3.html", dict)

""" movie view definition, returns a rendered .html
    file with aditional information in dict dictionary """
def ep4_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Episode 4 - A New Hope</h1>")
    dict = gen_dict_from_movie(1)
    return render(request, "episode4.html", dict)

""" movie view definition, returns a rendered .html
    file with aditional information in dict dictionary """
def ep5_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Episode 5 - The Empire Strikes Back</h1>")
    dict = gen_dict_from_movie(2)
    return render(request, "episode5.html", dict)

""" movie view definition, returns a rendered .html
    file with aditional information in dict dictionary """
def ep6_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Episode 6 - Return Of The Jedi</h1>")
    dict = gen_dict_from_movie(3)
    return render(request, "episode6.html", dict)

""" movie view definition, returns a rendered .html
    file with aditional information in dict dictionary """
def ep7_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Episode 7 - The Force Awakens</h1>")
    dict = gen_dict_from_movie(7)
    return render(request, "episode7.html", dict)


""" movie info view definition, returns a rendered .html
    file with aditional information in dict dictionary """
def more_info1(request, *args, **kwargs):
    #return HttpResponse("<h3>Want more info here</h3>")
    info_dict = gen_dict_info_from_movie(4)
    return render(request, "info1.html", info_dict)

""" movie info view definition, returns a rendered .html
    file with aditional information in dict dictionary """
def more_info2(request, *args, **kwargs):
    #return HttpResponse("<h3>Want more info here</h3>")
    info_dict = gen_dict_info_from_movie(5)
    return render(request, "info2.html", info_dict)

""" movie info view definition, returns a rendered .html
    file with aditional information in dict dictionary """
def more_info3(request, *args, **kwargs):
    #return HttpResponse("<h3>Want more info here</h3>")
    info_dict = gen_dict_info_from_movie(6)
    return render(request, "info3.html", info_dict)

""" movie info view definition, returns a rendered .html
    file with aditional information in dict dictionary """
def more_info4(request, *args, **kwargs):
    #return HttpResponse("<h3>Want more info here</h3>")
    info_dict = gen_dict_info_from_movie(1)
    return render(request, "info4.html", info_dict)

""" movie info view definition, returns a rendered .html
    file with aditional information in dict dictionary """
def more_info5(request, *args, **kwargs):
    #return HttpResponse("<h3>Want more info here</h3>")
    info_dict = gen_dict_info_from_movie(2)
    return render(request, "info5.html", info_dict)

""" movie info view definition, returns a rendered .html
    file with aditional information in dict dictionary """
def more_info6(request, *args, **kwargs):
    #return HttpResponse("<h3>Want more info here</h3>")
    info_dict = gen_dict_info_from_movie(3)
    return render(request, "info6.html", info_dict)

""" movie info view definition, returns a rendered .html
    file with aditional information in dict dictionary """
def more_info7(request, *args, **kwargs):
    #return HttpResponse("<h3>Want more info here</h3>")
    info_dict = gen_dict_info_from_movie(7)
    return render(request, "info7.html", info_dict)

""" generates a python dict with basic movie info consuming API data request for given a movie id """
def gen_dict_from_movie(id):

    movie = swapi.get_film(id)
    dict = {'title':movie.title, 'director':movie.director, 'producer':movie.producer, 'release':movie.release_date, 'crawl':movie.opening_crawl}
    return dict


""" generates a python dict with additional movie info consuming API data request for given a movie id """
def gen_dict_info_from_movie(id):

    movie = swapi.get_film(id)
    characters = []
    planets = []
    species = []
    spaceships = []
    vehicles = []

    """ get all characters from a movie and store them """
    for person in movie.characters:
        person_id = person.split('/')[5]
        characters.append((swapi.get_person(person_id)).name)

    #print (characters)
    #print(len(characters))

    """ get all planets from a movie and store them """
    for planet in movie.planets:
        planet_id = planet.split('/')[5]
        planets.append((swapi.get_planet(planet_id)).name)

    #print (planets)

    """ get all species from a movie and store them """
    for specie in movie.species:
        specie_id = specie.split('/')[5]
        species.append((swapi.get_species(specie_id)).name)

    """ get all starships from a movie and store them """
    for spaceship in movie.starships:
        ship_id = spaceship.split('/')[5]
        spaceships.append((swapi.get_starship(ship_id)).name)


    """ get all vehicles from a movie and store them """
    for vehicle in movie.vehicles:
        vehicle_id = vehicle.split('/')[5]
        vehicles.append((swapi.get_vehicle(vehicle_id)).name)



    dict = {'title':movie.title, 'characters':characters,
            'planets':planets, 'species':species,
            'spaceships':spaceships, 'vehicles':vehicles}
    return dict

""" get a film querry from API and return films in a tuple based
    list with episode id and title values as a dict """
def get_movies_list_by_ep():

    movie_set = swapi.get_all("films")
    movies = []

    for movie in movie_set.items:
        movies.append((movie.episode_id, movie.title))


    movies.sort(key=itemgetter(0))
    #print (movies)
    dict = {'movies':movies}

    return dict
