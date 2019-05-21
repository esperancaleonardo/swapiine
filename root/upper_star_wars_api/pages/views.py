from django.shortcuts import render, HttpResponse
# Create your views here.
def homepage_view(request, *args, **kwargs):
    #return HttpResponse("<h1>HomePage</h1><br/><h3>Welcome</h3></br>List of SW Movies:</br>Episode 1 - The Phantom Menace</br>Episode 2 - Attack Of The Clones</br>Episode 3 - Revenge Of The Sith</br>Episode 4 - A New Hope</br>Episode 5 - The Empire Strikes Back</br>Episode 6 - Return Of The Jedi</br>Episode 7 - The Force Awakens")
    return render(request, "index.html", {})

def ep1_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Episode 1 - The Phantom Menace</h1>")
    return render(request, "episode1.html", {})

def ep2_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Episode 2 - Attack Of The Clones</h1>")
    return render(request, "episode2.html", {})

def ep3_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Episode 3 - Revenge Of The Sith</h1>")
    return render(request, "episode3.html", {})

def ep4_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Episode 4 - A New Hope</h1>")
    return render(request, "episode4.html", {})

def ep5_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Episode 5 - The Empire Strikes Back</h1>")
    return render(request, "episode5.html", {})

def ep6_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Episode 6 - Return Of The Jedi</h1>")
    return render(request, "episode6.html", {})

def ep7_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Episode 7 - The Force Awakens</h1>")
    return render(request, "episode7.html", {})

def more_info1(request, *args, **kwargs):
    #return HttpResponse("<h3>Want more info here</h3>")
    return render(request, "info1.html", {})

def more_info2(request, *args, **kwargs):
    #return HttpResponse("<h3>Want more info here</h3>")
    return render(request, "info2.html", {})

def more_info3(request, *args, **kwargs):
    #return HttpResponse("<h3>Want more info here</h3>")
    return render(request, "info3.html", {})

def more_info4(request, *args, **kwargs):
    #return HttpResponse("<h3>Want more info here</h3>")
    return render(request, "info4.html", {})

def more_info5(request, *args, **kwargs):
    #return HttpResponse("<h3>Want more info here</h3>")
    return render(request, "info5.html", {})

def more_info6(request, *args, **kwargs):
    #return HttpResponse("<h3>Want more info here</h3>")
    return render(request, "info6.html", {})

def more_info7(request, *args, **kwargs):
    #return HttpResponse("<h3>Want more info here</h3>")
    return render(request, "info7.html", {})
