from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm



def user_logout(request):
    """Log out user"""
    logout(request)
    return redirect("/")


def register(request):
    """Register a new user."""
    if request.method != "POST":
        # Show empty form
        form = UserCreationForm()
    else:
        # Prosed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log in user
            login(request, new_user)
            return redirect("learning_logs:index")

    # Show empty of invalid form
    context = {"form": form}
    return render(request, "registration/register.html", context)