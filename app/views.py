from django.db.models import query
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect  # 301
import uuid # 使用uuid 字串以產生短網址
from .models import MappingUrl
# from django.shortcuts import redirect
import logging
# Create your views here.

async def index(request):
    # Index page and handle url data input.
    return render(request, 'index.html')


def redirect_to_page(request, shortenString):
    # Redirect to target url
    query_result = MappingUrl.objects.filter(shortenString=shortenString)
    if len(query_result)==1:
        originUrl = query_result[0].originUrl
        return HttpResponsePermanentRedirect(originUrl)
    else:
        return HttpResponseRedirect('/not_found/')

async def not_found(request):
    return render(request,'not_found.html')