from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import UserRegistrationForm
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages


#views starts here
def delete(request):
    if request.method == 'POST':
        u = User.objects.get(username = request.user.username)
        u.delete()
        messages.success(request, "Your account has been deleted")  
        return redirect('index')
    return render(request, 'account/delete.html')
def logout_view(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password( user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})