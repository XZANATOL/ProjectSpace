from django import template
from ..models import post

register = template.Library()

@register.simple_tag
def total_posts():
    return post.objects.filter(status="Published").count()