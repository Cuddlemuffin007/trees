from django.shortcuts import render, render_to_response

from trees_app.models import Tree


def index_view(request):
    all_trees = Tree.objects.all()
    return render_to_response('index.html', {'trees': list(all_trees)})


def data_view(request, capture):
    captured_tree = Tree.objects.get(name=capture)
    return render_to_response('data.html', {'tree': captured_tree})


def about_view(request):
    return render_to_response('about.html', {})

def nav_vew(request):
    return render_to_response('nav.html', {})

