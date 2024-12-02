from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record
from .forms import SignUpForm, AddRecordForm



def home(request):
    
    # getting records
    records= Record.objects.all() 
    # check to see if logging in
    if request.method=="POST":
        username=request.POST['username']
        password= request.POST['password']
        # Authenticate
        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have logged In")
            #print(res)
            return redirect('home')
        else:
            messages.error(request, "There was an error, try again!")
            return render(request, 'home.html', {})
    else:
        return render(request, 'home.html', {'records': records})


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, "You have been Logged Out")
    return redirect('home')


def customer_record(request, pk):
	if request.user.is_authenticated:
		#lookup on the records
		customer_records= Record.objects.get(id=pk)
		#if customer_records:
		return render(request, 'records.html', {'customer_records':customer_records})
		
	else:
		messages.error(request, "You must have logged in to view records!!!")
		return render(request, 'home.html', {})


def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record deleted successfully")
		return redirect('home')	 
	else:
		messages.error(request, "Some error happens while deleting")
		return redirect('home')


def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method== "POST":
			if form.is_valid():
				add_record=form.save()
				messages.success(request, "Record Added.....")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You must logged in...")
		return redirect('home')


def update_record(request, pk):
	if request.user.is_authenticated:
		current_record=Record.objects.get(id=pk)
		form=AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record is updated")
			return redirect('home')
		return render(request, 'update_record.html', {'form': form})
	else:
		messages.success(request, "You must be logged In")
		return redirect('home')