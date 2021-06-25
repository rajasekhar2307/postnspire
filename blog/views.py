from django.shortcuts import render, redirect
from .models import BlogPost
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.models import User

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

def createBlog(request):
	if request.method=='POST':
		blog_title = request.POST['blogtitle']
		blog_content = request.POST['blogcontent']

		blog = BlogPost(title = blog_title, content= blog_content, author = request.user)

		
		blog.save()

		print("Success! Blog Created")
		return redirect('/')

	else:
		return render(request, 'blog_new.html')
