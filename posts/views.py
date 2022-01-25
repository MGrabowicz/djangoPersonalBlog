from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.db.models.functions import datetime
from django.urls import reverse

from posts.forms import CreatePostForm, CreateTagForm, CreatePostTagForm, CreateCommentForm
from posts.models import Posts, Tags, PostsAndTags, Comments

paginatorNumber = 5


def homeView(request):
    latestPosts = Posts.objects.all().order_by('-addedAt')
    paginator = Paginator(latestPosts, paginatorNumber)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'latestPosts': page_obj
    }
    return render(request, "home.html", context)


def postsByTagView(request, pk):
    tag = Tags.objects.get(pk=pk)
    posts = Posts.objects.filter(postsandtags__tagID=tag).order_by('-addedAt')
    paginator = Paginator(posts, paginatorNumber)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'latestPosts': page_obj,
        'tag': tag,
    }
    return render(request, "posts/listByTags.html", context)


def createPostView(request):
    postCreateForm = CreatePostForm(request.POST, request.FILES)
    createTagForm = CreateTagForm(request.POST)
    createPostTagForm = CreatePostTagForm(request.POST)
    tagsList = []
    if postCreateForm.is_valid() and createTagForm.is_valid() and createPostTagForm.is_valid():
        instance = postCreateForm.save(commit=False)
        tags = instance.tags.lower().split(",")
        for tag in tags:
            try:
                tempTag = Tags.objects.get(tagContent=tag)
                tagsList.append(tempTag)
            except Tags.DoesNotExist:
                print("Adding new tag: " + tag)
                tagInstance = CreateTagForm(request.POST).save(commit=False)
                tagInstance.tagContent = tag
                tagInstance.save()
                tagsList.append(tagInstance)

        instance.author = request.user
        instance.addedAt = datetime.datetime.now()
        instance.updatedAt = datetime.datetime.now()
        instance.save()
        for tagId in tagsList:
            postAndTagInstance = CreatePostTagForm(request.POST).save(commit=False)
            postAndTagInstance.postID = instance
            postAndTagInstance.tagID = tagId
            postAndTagInstance.save()

        return HttpResponseRedirect(reverse('home'))
    else:
        print(postCreateForm.errors)

    context = {
        "postCreateForm": postCreateForm,
        "createTagForm": createTagForm,
        "createPostTagForm": createPostTagForm,
    }
    return render(request, "posts/createPost.html", context)


def detailPostView(request, pk):
    if request.POST.get('action') == 'post':
        result = ''
        commentID = request.POST.get('commentID')
        comment = Comments.objects.get(pk=commentID)
        if comment.likes.filter(id=request.user.id).exists():
            comment.likes.remove(request.user)
            comment.likeCount -= 1
            result = comment.likeCount
            comment.save()
        else:
            comment.likes.add(request.user)
            comment.likeCount += 1
            result = comment.likeCount
            comment.save()

        return JsonResponse({'result': result, })

    post = Posts.objects.get(pk=pk)
    tags = PostsAndTags.objects.all().filter(postID=post)
    tag = Tags.objects.all().filter(tagContent="porsche")
    comments = Comments.objects.filter(postID=post).order_by('addedAt')
    commentCreateForm = CreateCommentForm(request.POST)
    if commentCreateForm.is_valid():
        instance = commentCreateForm.save(commit=False)
        instance.authorID = request.user
        instance.postID = post
        instance.addedAt = datetime.datetime.now()
        instance.save()
        url = reverse('postDetail', kwargs={'pk': pk})
        return HttpResponseRedirect(url)
    context = {
        'post': post,
        'tags': tags,
        'comments': comments,
        'commentForm': commentCreateForm,
    }
    return render(request, "posts/detailPost.html", context)


def searchPosts(request):
    if request.GET:
        searchCriteria = request.GET.get('searchBar')
        searchResult = Posts.objects.filter(Q(title__icontains=searchCriteria) | Q(content__icontains=searchCriteria) | Q(postsandtags__tagID__tagContent=searchCriteria)).order_by('-addedAt').distinct()
        print(searchResult)
        context = {
            'searchResult': searchResult,
        }
        return render(request, "posts/searchPosts.html", context)
    return render(request, "posts/searchPosts.html")
