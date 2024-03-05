from django import template

from likes.models import ServiceLikes

register = template.Library()

@register.simple_tag(takes_context=True)
def is_liked(context, blog_post_id):
    request = context['request']
    try:
        blog_likes = ServiceLikes.objects.get(blog_post__id=blog_post_id, liked_by=request.user.id).like
    except Exception as e:
        blog_likes = False
    return blog_likes


@register.simple_tag()
def count_likes(blog_post_id):
    # return ServiceLikes.objects.filter(blog_post__id='', like=True).count()
    return ServiceLikes.objects.filter(blog_post__id=blog_post_id, like=True).count()


@register.simple_tag(takes_context=True)
def blog_likes_id(context, blog_post_id):
    request = context['request']
    return ServiceLikes.objects.get(blog_post__id=blog_post_id, liked_by=request.user.id).id
