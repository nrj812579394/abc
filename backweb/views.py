from django.shortcuts import render

from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from backweb.Artform import AddArtForm, Register, EditArt
from backweb.models import Article, MyUser
from django.core.paginator import Paginator


def add_art(request):
    if request.method == 'GET':
        return render(request, 'backweb/add_article.html')
    if request.method == 'POST':
        form = AddArtForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            desc = form.cleaned_data['desc']
            content = form.cleaned_data['content']
            icon = form.cleaned_data['icon']
            Article.objects.create(title=title, desc=desc, content=content, icon=icon)
        # 创建成功后，返回文章列表
            return HttpResponseRedirect(reverse('art:art_list'))
        else:
            return render(request, 'backweb/add_article.html', {'form': form})


def art(request):
    if request.method == 'GET':
        page = int(request.GET.get('page', 1))
        articles = Article.objects.all()
        paginator = Paginator(articles, 3)
        pages = paginator.page(page)
        return render(request, 'backweb/art.html', {'pages': pages})


def edit_art(request, id):
    if request.method == 'GET':
        article = Article.objects.filter(pk=id).first()
        return render(request, 'backweb/add_article.html', {'article': article})
    if request.method == 'POST':
        form = EditArt(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['desc']
            content = form.cleaned_data['content']
            icon = form.cleaned_data['icon']
            article = Article.objects.filter(pk=id).first()
            article.title = title
            article.desc = desc
            article.content = content
            if icon:
                article.icon = icon
            article.save()
            return HttpResponseRedirect(reverse('art:art_list'))
        else:
            article = Article.objects.filter(pk=id).first()
            return render(request, 'backweb/add_article.html', {'form': form, 'article': article})


def del_art(request, id):
    if request.method == 'GET':
        Article.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('art:art_list'))


def register(request):
    if request.method == 'GET':
        return render(request, 'backweb/register.html')

    if request.method == 'POST':
        form = Register(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            u_name = MyUser.objects.filter(username=username).first()
            if u_name:
                err_name = '该账号已经注册过了'
                return render(request, 'backweb/register.html', {'err_name': err_name})
            if password != password2:
                err_name = '两次密码不一致！'
                return render(request, 'backweb/register.html', {'err_name': err_name})
            MyUser.objects.create(username=username, password=password)
            return HttpResponseRedirect('/backweb/login/')
        else:
            return render(request, 'backweb/register.html', {'form': form})

        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # password2 = request.POST.get('password2')
        # u_name = MyUser.objects.filter(username=username).first()
        # if u_name:
        #     err_name = '该账号已经注册过了'
        #     return render(request, 'register.html', {'err_name': err_name})
        # if password and password2:
        #     if password != password2:
        #         err_name = '两次密码不一致'
        #         return render(request, 'register.html', {'err_name': err_name})
        # else:
        #     err_name = '密码不能为空'
        #     return render(request, 'register.html', {'err_name': err_name})
        # MyUser.objects.create(username=username, password=password)
        # return HttpResponseRedirect('/login/')


def login(request):
    if request.method == 'GET':
        return render(request, 'backweb/login.html')

    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = MyUser.objects.filter(username=u, password=p).first()
        if not user:
            err_name = '账号或者密码错误'
            return render(request, 'backweb/login.html', {'err_name': err_name})
        request.session['user_id'] = user.id
        return HttpResponseRedirect('/backweb/art/')
