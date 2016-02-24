from django.shortcuts import render, render_to_response


def index_view(request):
    return render_to_response('index.html', {})


def data_view(request):
    return render_to_response('data.html', {})


def about_view(request):
    return render_to_response('about.html', {})

