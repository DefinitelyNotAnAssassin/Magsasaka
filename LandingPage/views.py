from django.shortcuts import render, redirect
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request, 'LandingPage/admin_index.html')
        else:
            return redirect('virtual_id')
    else: 
        return render(request, 'LandingPage/index.html')
