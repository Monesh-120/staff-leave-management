from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from myapp.models import Profile
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
	return render(request,'myapp/home.html')

def register_view(request):
	if request.method=='POST':
		# print(request.POST)
		username=request.POST['username']
		password=request.POST['password']
		role=request.POST['role']
		# print(username,role,password)
		user=User.objects.create_user(username=username,password=password)
		Profile.objects.create(user=user,role=role)
		return redirect('login')
	return render(request,'myapp/register.html')

def login_view(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		print(username,password)
		user=authenticate(request,username=username,password=password)
		print(user)
		if user:
			login(request,user)
			if user.profile.role=='admin':
				return redirect('admin_dashboard')
			else:
				return redirect('user_dashboard')
		else:
			print("Invalid Credentials")
	return render(request,'myapp/login.html')

@login_required(login_url='login')
def user_dashboard(request):
	return render(request,'myapp/user_dashboard.html')

@login_required(login_url='login')
def admin_dashboard(request):
	if request.user.profile.role != 'admin':
		return redirect('user_dashboard')
	return render(request,'myapp/admin_dashboard.html')

def logout_view(request):
	logout(request)
	return redirect('login')

# @login_required(login_url='login')
# def admin_leave_management(request):
# 	return render(request,'myapp/admin_LM.html')

# def leave_approval(request):
# 	return render(request,'myapp/leave_approval.html')

@login_required
def manage_staff(request):
	if request.user.profile.role != 'admin':
		return redirect('user_dashboard')
	
	staff_list=User.objects.filter(profile__role='staff')
	for i in staff_list:
		n=i.username[0].upper()
	d={'staff_list':staff_list,'n':n}
	return render(request,'myapp/manage_staff.html',d)

@login_required
def add_staff(request):
	if request.user.profile.role != 'admin':
		return redirect('user_dashboard')
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=User.objects.create_user(username=username,password=password)
		Profile.objects.create(user=user,role='staff')
		return redirect('manage_staff')
	return render(request,'myapp/add_staff.html')

@login_required
def edit_staff(request,id):
	if request.user.profile.role != 'admin':
		return redirect('user_dashboard')
	user=get_object_or_404(User,id=id)
	if request.method=='POST':
		user.username=request.POST['username']
		user.save()
		return redirect('manage_staff')
	return render(request,'myapp/edit_staff.html',{'user':user})

@login_required
def delete_staff(request,id):
	if request.user.profile.role != 'admin':
		return redirect('user_dashboard')
	user=get_object_or_404(User,id=id)
	user.delete()
	return redirect('manage_staff')