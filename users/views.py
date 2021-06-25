from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def signup(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']

		print("inside signup def ")
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
			return redirect('/')
		else:
			messages.error(request, "Invalid Credentials!")
			return redirect('login')

	else:
		return render(request, 'login.html')




def logout(request):
	auth.logout(request)
	return redirect('/')