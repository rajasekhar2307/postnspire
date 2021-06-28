from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import BlogPost
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone


# Create your views here.
def post(request):
	context = {
		'blogs': BlogPost.objects.all()
	}
	return render(request, 'blog.html', context)

def index(request):
	context = {
		'blogs': BlogPost.objects.all()
	}
	return render(request, 'index.html', context)


class BlogPostListView(ListView):
	model = BlogPost
	template_name = 'index.html'
	context_object_name = 'blogs'
	ordering = ['-date_posted']


class BlogPostDetailView(DetailView):
	model = BlogPost
	template_name = 'blog_detail.html'

# class BlogPostCreateView(CreateView):
# 	model = BlogPost
# 	template_name = 'blog_new.html'
# 	fields = ['title', 'content']


@login_required(login_url='/users/login/')
def createBlog(request):
	if request.method=='POST':
		blog_title = request.POST['blogtitle']
		blog_content = request.POST['blogcontent']
		blog_image = request.FILES['image']
		blog = BlogPost(title = blog_title, content= blog_content, author = request.user, image = blog_image, date_posted=timezone.now())

		
		blog.save()

		print("Success! Blog Created")
		return redirect('/')

	else:
		return render(request, 'blog_new.html')


@login_required(login_url='/users/login/')
def editBlog(request, pk):

	blog = BlogPost.objects.get(pk=pk)
	if(request.user != blog.author):
		messages.error(request, "Cannot Update")
		return redirect(f'/blog/{blog.pk}')

	if request.method=='POST':
		# print(f"request made here is : {BlogPost.objects.filter(pk = pk)}")
		blog.title = request.POST['blogtitle']
		blog.content = request.POST['blogcontent']
		
		blog.save()
		messages.success(request, "Blog Updated Successfully!")
		return redirect(f'/blog/{blog.pk}')

	else:
		context = {
			'blog':blog
		}
		return render(request, 'blog_update.html',context)

# class BlogPostCreateView(LoginRequiredMixin,CreateView):
# 	model = BlogPost
# 	template_name = 'blog_new.html'
# 	fields = ['title', 'content']

@login_required(login_url='/users/login/')
def deleteBlog(request, pk):
	blog = BlogPost.objects.get(pk=pk)
	if(request.user != blog.author):
		messages.error(request, "You can't delete other's post!")
		return redirect(f'/blog/{blog.pk}')
	else:
		blog.delete()
		return redirect("/")



class BlogPostUpdateView(LoginRequiredMixin,UpdateView):
	model = BlogPost
	template_name = 'blog_update.html'
	fields = ['title', 'content']
