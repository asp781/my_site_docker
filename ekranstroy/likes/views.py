from django.shortcuts import redirect, render
from django.views.generic import View

from django.contrib.auth.models import User
from price.models import Service
from .models import ServiceLikes

class AddLikeView(View):
    def post(self, request, *args, **kwargs):

        blog_post_id = request.POST.get('blog_post_id')
        user_id = request.POST.get('user_id')
        url_form = request.POST.get('url_form')

        user_inst = User.objects.get(id=user_id)
        blog_post_inst = Service.objects.get(id=blog_post_id)

        try:
            blog_like_inst = ServiceLikes.objects.get(blog_post=blog_like_inst, liked_by=user_inst)
        except Exception as e:
            blog_like = ServiceLikes(
                blog_post=blog_post_inst,
                liked_by=user_inst,
                like=True
            )
            blog_like.save()

        return redirect(url_form)


class RemoveLikeView(View):
    def post(self, request, *args, **kwargs):
        blog_likes_id = int(request.POST.get('blog_likes_id'))
        url_form = request.POST.get('url_form')

        blog_like = ServiceLikes.objects.get(id=blog_likes_id)
        blog_like.delete()

        return redirect(url_form)


def my_likes(request):
    user_id = request.user.id
    id_servise_by_user = ServiceLikes.objects.filter(liked_by_id=user_id)
    list_id = [x.blog_post_id for x in id_servise_by_user]
    servises = Service.objects.filter(pk__in=list_id)
    template_name = 'my_likes.html'
    return render(request, template_name, context={'servises': servises})
