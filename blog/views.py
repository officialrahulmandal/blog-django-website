# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from .models import post
from django.utils import timezone
# Create your views here.
def post_list(request):
    posts=post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #posts = post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html',{'posts':posts})
def post_detail(request,pk):
    past=get_object_or_404(post,pk=pk)
    return render(request,'blog/post_detail.html',{'post':past})
