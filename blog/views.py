# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404,redirect
from .models import post
from .forms import PostForm
from django.utils import timezone
# Create your views here.
def post_list(request):
    posts=post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #posts = post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html',{'posts':posts})
def post_detail(request,pk):
    past=get_object_or_404(post,pk=pk)
    return render(request,'blog/post_detail.html',{'post':past})
def post_new(request):
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.published_date=timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=PostForm()
    return render(request,'blog/post_edit.html',{'form':form})
def post_edit(request,pk):
    past=get_object_or_404(post,pk=pk)
    if request.method=="POST":
        form = PostForm(request.POST,instance=past)
        if form.is_valid():
            past=form.save(commit=False)
            past.author = request.user
            past.published_date=timezone.now()
            past.save()
            return redirect('post_detail',pk=past.pk)
    else:
            form =PostForm(instance=past)
    return render(request,'blog/post_edit.html',{'form':form})
