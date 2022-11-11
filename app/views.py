from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Confession
from django.contrib.auth.models import User
#import HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        return render(request, 'app/index.html')
def addConfession(request, username):
    if User.objects.filter(username=username):
        print('user exists')
        if request.method == 'POST':
            user = User.objects.get(username=username)

            confession = request.POST['confession']
            user = user
            Confession.objects.create(confession=confession, user=user)
            return HttpResponseRedirect(request.path_info)
            messages.success(request, 'Confession sent!')
            context= {
            'user': user
            }
        return render(request, 'app/addConfession.html', {'username': username})
    else:
        return render(request, 'app/dont.html', {'username': username})
@login_required
def profile(request):
    user = request.user
    confessions = user.confessions.all().order_by('-date')
    context = {
        'user': user,
        'confessions': confessions
    }
    
    return render(request, 'app/profile.html', context)

