from django.shortcuts import render
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request, 'LandingPage/admin_index.html')
        else:
            return render(request, 'LandingPage/user_index.html')
    else: 
        return render(request, 'LandingPage/index.html')
