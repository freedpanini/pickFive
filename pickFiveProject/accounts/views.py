from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as login_auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import AccountRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from groups.models import *


#################### index#######################################
@login_required
def index(request):
    """
    Renders the index page with the available groups and user groups.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered index page.
    """

    # get the available groups and user groups
    available_groups = Group.objects.filter(IsPublic=True, IsActive=True)
    user_groups = GroupXAccount.objects.filter(Account=request.user).select_related()

    # render the index page with the available groups and user groups
    context = {
        "title": "index",
        "available_groups": available_groups,
        "user_groups": user_groups,
    }
    return render(request, "index.html", context)


########### register here #####################################
def register(request):
    """
    View function for user registration.

    This function handles the user registration process. It validates the registration form,
    creates a new user account, and redirects the user to the login page upon successful registration.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.

    """

    # check if the request method is POST
    if request.method == "POST":
        
        # create a new user account
        form = AccountRegisterForm(request.POST)

        # validate the registration form
        if form.is_valid():

            # save the user account, get the username and email, and display a success message
            account = form.save()
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            messages.success(
                request, f"Your account has been created! You are now able to log in."
            )
            return redirect("login")

    # if the request method is not POST, render the registration form
    else:
        form = AccountRegisterForm()

    return render(request, "register.html", {"form": form, "title": "register here"})


################ login forms###################################################
def login(request):
    """
    View function for handling user login.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.

    """

    # check if the request method is POST
    if request.method == "POST":
        # AuthenticationForm_can_also_be_used__
        # obtain the username and password from the request
        username = request.POST["username"]
        password = request.POST["password"]

        # authenticate the user
        user = authenticate(request, username=username, password=password)

        # if the user exists, log in the user and redirect to the index page
        if user is not None:
            form = login_auth(request, user)
            return redirect("index")
        else:
            # if the user does not exist, display an error message
            messages.info(request, f"account does not exist, please sign in")

    # if the request method is not POST, render the login form
    form = AuthenticationForm()

    return render(request, "login.html", {"form": form, "title": "log in"})
