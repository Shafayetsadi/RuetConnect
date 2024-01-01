from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.db.models import F
from django.http import Http404
from .models import Post, Vote, Thread

# Create your views here.

def about(request):
    return HttpResponse('<h1>Campus About</h1>')

def thread(request, thread_name):
    try:
        thread = get_object_or_404(Thread, thread_name=thread_name)
    except Http404:
        return HttpResponse('<h1>Thread not found</h1>')
    context = {'thread': thread}
    return render(request, 'campus/thread.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'campus/index.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Post.objects.all()
        else:
            return Post.objects.filter(thread__thread_name='ruet')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False





def upvote(request, pk):
    # check if the user is authenticated
    if not request.user.is_authenticated:
        messages.error(request, f'You need to login first.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    post = get_object_or_404(Post, pk=pk)
    if Vote.objects.filter(user=request.user, post=post).exists():
        vote = Vote.objects.get(user=request.user, post=post)
        if vote.vote_type == 1:
            vote.delete()
            messages.success(request, f'Vote removed.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        elif vote.vote_type == -1:
            vote.vote_type = 1
            vote.save()
            messages.success(request, f'Upvoted.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            pass
    else:
        vote = Vote(user=request.user, post=post, vote_type=1)
        vote.save()
        messages.success(request, f'Upvoted.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def downvote(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, f'You need to login first.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    post = get_object_or_404(Post, pk=pk)
    if Vote.objects.filter(user=request.user, post=post).exists():
        vote = Vote.objects.get(user=request.user, post=post)
        if vote.vote_type == -1:
            vote.delete()
            messages.error(request, f'Vote removed.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        elif vote.vote_type == 1:
            vote.vote_type = -1
            vote.save()
            messages.success(request, f'Downvoted.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            pass
    else:
        vote = Vote(user=request.user, post=post, vote_type=-1)
        vote.save()
        messages.success(request, f'Vote successful.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def search(request):
    query = request.GET.get('query', '')
    print(f'\n\n\nthe query: {query}\n\n\n')

    if query:
        post = Post.objects.filter(title__icontains=query)
    else:
        post = []
    
    context = {'matched_posts': post}
    return render(request, 'campus/_search_results.html', context)