from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

def user_login(request):
    if  request.user.is_authenticated(): #if user is logged in
        return render(request, 'tracktivityPetsWebsite/login.html')
    
    elif request.method == 'POST': #if http request was made with POST type
        try:
            username = request.POST['username'] #get and store username
        except:
            return render(request, 'tracktivityPetsWebsite/login.html', { "error_message": "No username" })
        
        try:
            password = request.POST['password'] #get and store password
        except:
            return render(request, 'tracktivityPetsWebsite/login.html', { "error_message": "No password" })
        
        user = authenticate(username=username, password=password) #django method to see if user exists in database
        if user is not None:
            if user.is_active: #if the account is activated
                login(request, user) #log the user into a session
                return render(request, 'tracktivityPetsWebsite/login.html')
            else:
                return render(request, 'tracktivityPetsWebsite/login.html')
        else:
            return render(request, 'tracktivityPetsWebsite/login.html', { "error_message": "Incorrect username/password combination" }) #no user was found
        
    else:
        return render(request, 'tracktivityPetsWebsite/login.html')