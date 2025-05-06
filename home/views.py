from datetime import datetime
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm

from .models import Watch
from .forms import CommentForm, FeedbackForm, WatchForm


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            rating_site = form.cleaned_data['rating_site']
            rating_design = form.cleaned_data['rating_design']
            suggestions = form.cleaned_data['suggestions']
            recommend = form.cleaned_data['recommend']
            feedback_type = form.cleaned_data['feedback_type']

            return render(request, 'home/pool.html', {
                'form': form,
                'rating_site': rating_site,
                'rating_design': rating_design,
                'suggestions': suggestions,
                'recommend': recommend,
                'feedback_type': feedback_type,
                'message': "Спасибо за ваш отзыв!"
            })
    else:
        form = FeedbackForm()

    return render(request, 'home/feedback_form.html', {'form': form})


def registration(request):
    assert isinstance(request, HttpRequest)

    if request.method == "POST":
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_staff = False
            reg_f.is_active = True
            reg_f.is_superuser = False
            reg_f.date_joined = datetime.now()
            reg_f.last_login = datetime.now()
            reg_f.save()
            return redirect('home:login')  
    else:
        regform = UserCreationForm()

    return render(
        request,
        'registration/registration.html',
        {
            'regform': regform,
            'year':datetime.now().year,
        }
    )


def logout_user(request):
    logout(request)
    return redirect("home:home")


def blog(request):
    posts = Watch.objects.all().order_by('-published')
    return render(request, 'home/blog.html', {'posts': posts})


def watch_detail(request, parameter):
    watch = get_object_or_404(Watch, pk=parameter)
    comments = watch.comments.all().order_by('-date')

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.watch = watch
                comment.author = request.user
                comment.save()
        else:
            return redirect('home:login')
    else:
        form = CommentForm()

    return render(request, 'home/blogpost.html', {
        'watch': watch,
        'comments': comments,
        'form': form,
    })


def add_watch(request):
    if request.method == 'POST':
        form = WatchForm(request.POST, request.FILES)
        if form.is_valid():
            watch = form.save(commit=False)
            watch.author = request.user
            watch.save()
            return redirect('home:blog') 
    else:
        form = WatchForm()
    return render(request, 'home/add_blog.html', {'form': form})