#coding:utf-8
from django.shortcuts import render, render_to_response
import time
from django.template import Template, Context
from django.http import HttpResponse
from django.template.loader import get_template
# Create your views here.
# def index (request):
#
#     return render(request, 'index.html')
#

def index(request):
    t = get_template('index.html')
    detail_list = 0
    c = Context({'detail_list': detail_list},{})
    return HttpResponse(t.render(c))

# def Current_Year(request):
#     Year = time.strftime('%Y', time.localtime(time.time()))
#     # t = get_template('index.html')
#     # html = t.render( Context({'Year': Year}))
#     return render_to_response('index.html',{'Year': Year} )
