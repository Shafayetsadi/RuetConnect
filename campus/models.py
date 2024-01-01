from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from markdownx.models import MarkdownxField

# Create your models here.

class Thread(models.Model):
    thread_name = models.CharField(max_length=100)
    thread_title = models.CharField(max_length=100, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    subscribers = models.ManyToManyField(User, through='Subscribed', related_name='subscribed_threads')
    image = models.ImageField(default='thread.jpg', upload_to='thread_pics')

    def __str__(self):
        return self.thread_name

    def save(self, *args, **kwargs):
        if not self.thread_title:
            self.thread_title = self.thread_name.capitalize()
        super().save(*args, **kwargs)
        


class Post(models.Model):
    title = models.CharField(max_length=100)
    # content = models.TextField()
    content = RichTextField(blank=True, null=True)
    body = MarkdownxField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, related_name='posts', on_delete=models.CASCADE, null=True)
    voters = models.ManyToManyField(User, through='Vote', related_name='voted_posts')

    def get_vote_count(self):
        return self.votes.filter(vote_type=1).count() - self.votes.filter(vote_type=-1).count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

    def save(self, *args, **kwargs):
        if not self.thread:
            default_thread, created = Thread.objects.get_or_create(name='ruet')
            self.thread = default_thread
        super().save(*args, **kwargs)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, default=Thread)

    def __str__(self):
        return self.author.username+"->"+self.post.title
    

class Subscribed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)

    def __str__(self):
        return self.thread.thread_name+"<-"+self.user.username

    class Meta:
        unique_together = ('user', 'thread')


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='votes')
    # a field to store tyoe of vote
    # 1 for upvote
    # -1 for downvote
    # 0 for no vote
    vote_type = models.IntegerField(default=0)

    def __str__(self):
        return self.post.title+"<-"+self.user.username

    class Meta:
        unique_together = ('user', 'post')