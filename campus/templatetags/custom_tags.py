from django import template

register = template.Library()

from campus.models import Post, Vote

@register.simple_tag
def get_user_vote(post_id, user_id):
    user_vote = Vote.objects.filter(post=post_id, user=user_id).first()    
    return user_vote
