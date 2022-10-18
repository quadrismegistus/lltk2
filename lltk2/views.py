
# -------------------
# Views and routes
# -------------------

@route('', name='index')
def show_index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


@route('blog/<int:post_id>/', name='post')
def show_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post.html', {'post': post})


@route(r'^regex/(.*)$', regex=True)
def regex_view(request, value):
    return HttpResponse(value)


@route('class-based/')
class ClassBasedView(View):
    def get(self, request):
        return HttpResponse('Hello from class-based view')
