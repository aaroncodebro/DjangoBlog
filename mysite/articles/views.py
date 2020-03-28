from django.shortcuts import render, redirect
from .models import Article 
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms


def article_list(request):
	articles = Article.objects.all().order_by('-date')
	return render(request, 'articles/article_list.html',{'articles':articles})

def dashboard(request):
	user = request.user
	articles = Article.objects.filter(author = user)
	return render(request, 'articles/dashboard.html',{'articles':articles})



def article_detail(request, article_id):
	article = Article.objects.get(id = article_id)
	return render(request, 'articles/article_detail.html', {'article': article})

@login_required(login_url="/accounts/login/")
def article_create(request):
	if request.method =='POST':
		form = forms.CreateArticle(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			return redirect('articles:list')
	else:
		form = forms.CreateArticle()
	return render(request, 'articles/article_create.html', {'form':form})

@login_required(login_url="/accounts/login/")
def article_edit(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:dashboard')
        else:
            form = forms.CreateArticle(instance=article)
    else:
        form = forms.CreateArticle(instance=article)
    return render(request, 'articles/article_edit.html', {'form':form , 'article':article })
	