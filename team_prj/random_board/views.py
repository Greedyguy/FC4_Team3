from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from .models import Post
from .models import Category
from .models import Comment


def list_posts(request):
    # 단순조회
    if request.method == 'GET':
        posts = Post.rand_generate_post()
    # keep으로 필터링 해 보기 사용시!
    elif request.method == 'POST':
        posts = Post.filtered_post()

    return render(request, 'list.html', {
        'posts': posts,

    })


# pk를 인자로 받을 경우에는 update, 그 외에는 create
def create_post(request):
    # Get일 경우 글 수정
    categories = Category.objects.all()
    ctx = {}
    if request.method == 'GET':
        ctx = {
            'category': categories,
        }
    # Post일 경우 글 작성
    elif request.method == 'POST':
        pass

    return render(request, 'edit.html', ctx)


def edit_post(request, pk):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=pk)
        categories = Category.objects.all()
    else:
        return create_post(request)

    return render(request, 'edit.html', {
        'post': post,
        'categories': categories,
    })


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('rpost:list_post')

    return render(request, 'delete.html', {
        'post': post,
    })


def view_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        pass
    return render(request, 'view.html', {
        'post': post,
    })


def create_comment(request, pk):
    comment = Comment()
    comment.content = request.POST['comment_writer']
    comment.post_id = pk
    comment.save()

    return redirect('rpost:view_post', pk=pk)
