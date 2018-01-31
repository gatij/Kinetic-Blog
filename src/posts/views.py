from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect,Http404
from .models import Post,Author,Category,Tag,upload_location
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.db.models import Q
# Create your views here.


def PostHome(request):
	queryset_list=Post.objects.filter(draft=False).filter(publish__lte=timezone.now())
	query=request.GET.get('q')
	if query:
		queryset_list=queryset_list.filter(
			Q(title__icontains=query)|
			Q(content__icontains=query)|
			Q(author__name__icontains=query)|
			Q(category__name__icontains=query)|
			Q(tags__name__icontains=query)
			).distinct()
	paginator = Paginator(queryset_list, 5)
	page = request.GET.get('page')
	queryset = paginator.get_page(page)
	context={'queryset':queryset,
              
	}
	return render(request,'posts/index_kinetic.html',context)

def PostCreate(request):
	form=PostForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.success(request,"Created Successfully")
		return HttpResponseRedirect(instance.get_absolute_url())
	
	context={
	'form':form,
	}
	return render(request,'posts/post_create.html',context)

def PostDetail(request,obj_slug):
	instance=get_object_or_404(Post,slug=obj_slug)
	if instance.draft:
		raise Http404
	context={'obj':instance,}
	return render(request,'posts/post_kinetic.html',context)

def PostUpdate(request,obj_slug):
	instance=get_object_or_404(Post,slug=obj_slug)
	form=PostForm(request.POST or None,request.FILES or None,instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.success(request,"updated Successfully")
		return HttpResponseRedirect(instance.get_absolute_url())
	context={'obj':instance,
	         'form':form,
	         }
	return render(request,'posts/post_create.html',context)

def PostDelete(request,obj_slug):
	instance=get_object_or_404(Post,slug=obj_slug)
	instance.delete()
	messages.success(request,"Deleted Successfully")
	return redirect('posts:index')	


def TagDetail(request,tag_slug):
	instance=get_object_or_404(Tag,slug=tag_slug)
	tag=instance.post_set.all()
	context={'tag':tag,}
	return render(request,'posts/tag_posts.html',context)
