# coding=utf-8
from django.http.response import HttpResponse
from django.template.context import RequestContext
from django.shortcuts import render_to_response

def index(request):
    context = RequestContext(request)
    return render_to_response("index.html", context)