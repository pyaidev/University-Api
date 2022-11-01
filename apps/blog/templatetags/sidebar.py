from django.template import Library
from ..models import Tag, Category, Blog

register = Library()

@register.simple_tag
def sidebar_posts():
    return Blog.objects.all().order_by('-id')[:3]


@register.simple_tag
def sidebar_categories():
    return Category.objects.all()


@register.simple_tag
def sidebar_tags():
    return Tag.objects.all()


