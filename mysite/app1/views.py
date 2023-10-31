from imaplib import _Authenticator
from multiprocessing import AuthenticationError
from django import template
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect



def create(request):
    return render(request, 'Createuser.html')

def update(request):
    return render(request, 'teamupdate.html')

def timesheet(request):
    return render(request, 'Timesheet.html')

def sales(request):
    return render(request, 'sales.html')

def reqcan(request):
    return render(request, 'reqcan.html')



def login(request):
    if request.method == 'POST':
        id = request.POST['id']
        firstname = request.POST['firstname']
        user = AuthenticationError(request, id=id, firstname=firstname)
        if user is not None:
            login(request, user)
            return redirect('create')  # Replace 'home' with your desired URL
        else:
            # Handle invalid login attempt
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})

    return render(request, 'login.html')

# def logout(request):
#     logout(request)
#     return redirect('login')  # Redirect to your login page




# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect

# def create(request):
#     return render(request, 'Createuser.html')

# def update(request):
#     return render(request, 'teamupdate.html')

# def timesheet(request):
#     return render(request, 'Timesheet.html')

# def sales(request):
#     return render(request, 'sales.html')






# from django.contrib.auth import authenticate, login

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['id']  # Use the 'id' field as the username
#         password = request.POST['firstname']  # Use the 'firstname' field as the password
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             # Successful login, redirect to a success page or dashboard.
#         else:
#             # Handle invalid login attempt
#             # You can return an error message or render the login page with an error message.
#             return render(request, 'login.html', {'error_message': 'Invalid credentials'})

#     return render(request, 'login.html')



















