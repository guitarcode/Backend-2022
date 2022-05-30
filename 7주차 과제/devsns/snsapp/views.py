from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm
from .models import Post, Comment

def home(request) :
    return render(request, "index.html")

def posttable(request) :
    posts = Post.objects.filter().order_by('-date')
    return render(request, "tables.html", {'posts':posts})

def postcreate(request) :
    if request.method == "POST" or request.method== "FILES":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posttable')
    else:
        form = PostForm()
    #form이라는 변수를 'form'이라는 key값에 value로 담아서 post_form.html에 정보를 전달
    return render(request, 'post_form.html', {'form':form})

def postdetail(request, post_id) :
    post_detail = get_object_or_404(Post,pk=post_id)
    comment_form = CommentForm()
    return render(request, 'postdetail.html', {'post_detail':post_detail,'comment_form':comment_form})

def commentcreate(request, post_id) :
    mid_form = CommentForm(request.POST)
    if mid_form.is_valid():
        fin_form = mid_form.save(commit='False')
        fin_form.post = get_object_or_404(Post, pk=post_id)
        fin_form.save()
    return redirect('postdetail', post_id)


# Create your views here.
