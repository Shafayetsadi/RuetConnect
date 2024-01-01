from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = UserRegisterForm(request.POST)
        # Check if form is valid
        if form.is_valid():
            # Save the form data to the database
            form.save()
            # Redirect to the home page
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def update_profile(request):
    if request.method =='POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                    request.FILES, 
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            # Save the form data to the database
            u_form.save()
            p_form.save()
            # Display a success message
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
            'u_form': u_form,
            'p_form': p_form
            }
    return render(request, 'users/profile_update.html', context)

@login_required
def profile(request):
    return render(request, 'users/profile.html')