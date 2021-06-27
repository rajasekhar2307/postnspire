from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blog.models import BlogPost

# Create your views here.
def signup(request):
	
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']

		if username == "" or email == "" or password == "":
			messages.error(request, "Enter all details!")
			return render(request, 'signup.html')

		if User.objects.filter(username = username).exists() or User.objects.filter(email = email).exists():
			print("username/email already taken")
			messages.error(request, "Username/Email is already taken")
			return redirect('signup')
		else:
			user = User.objects.create_user(username = username, email = email,password= password)
			user.save()
			messages.success(request, "Account Created Succesfully!\nLogin to continue.")
			return redirect('login')

	else:
		return render(request, 'signup.html')





def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username = username, password = password)

		if user is not None:
			auth.login(request, user)
			print("logged in ")
			if 'next' in request.POST:
				return redirect(request.POST.get('next'))
			else:
				return redirect('/')
		else:
			messages.error(request, "Invalid Credentials!")
			return redirect('login')

	else:
		return render(request, 'login.html')




def logout(request):
	auth.logout(request)
	return redirect('/')



def profile(request, username):
	if User.objects.filter(username = username):
		user = User.objects.get(username= username)
		count = BlogPost.objects.filter(author = user).count()
		print(count)
		context = {
			'user':user,
			'blogcount': count
		}
		return render(request, 'profile.html', context)
	else:
		return redirect('/')
	

@login_required(login_url='/users/login/')
def editProfile(request, username):

	if request.method == 'POST':
		print(request.user.username)
		if not User.objects.get(username = username).username == request.user.username:
			return redirect('/')
		user = request.user

		user.username = request.POST['username']
		user.email = request.POST['email']

		profile = user.profile

		profile.name = request.POST['name']
		profile.website = request.POST['website']
		profile.bio = request.POST['bio']
		if request.FILES:
			profile.image = request.FILES['image']

		user.save()
		profile.save()
		messages.success(request, "Profile Updated!")
		return render(request, 'edit_profile.html')


	else:
		user = User.objects.get(username= username)
		context = {
			'user':user
		}
		if User.objects.filter(username = username) and User.objects.get(username = username).username == request.user.username:
			return render(request, 'edit_profile.html', context)
		else:
			messages.error(request, "You cannot edit others profile")
			return render(request, 'profile.html', context)
		