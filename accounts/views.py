from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

from .models import Contact, Reader, Librarian
from requisitions.models import Requisition
from .forms import ContactForm, ProfileEditForm


def is_admin(user):
    return user.is_superuser


def loginUser(request):
    if request.user.is_authenticated:
        return redirect("profile")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = Contact.objects.get(username=username)
        except:
            messages.error(request, "Nome de utilizador não existente.")
            return render(request, "accounts/login.html")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("profile")
        else:
            messages.error(
                request, "Nome de utilizador ou palavra-passe incorretos.")

    return render(request, "accounts/login.html")


def logoutUser(request):
    logout(request)
    messages.info(request, "Sessão encerrada com sucesso.")
    return redirect("login")


@login_required(login_url="login")
@user_passes_test(is_admin)
def registerLibrarian(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            librarian = Librarian.objects.create(user=user)
            messages.success(request, "Bibliotecário criado com sucesso.")

            return redirect("dashboard")
        else:
            messages.error(request, "Ocorreu um erro durante o registo")

    context = {
        "form": form,
        "page": "librarian"
    }

    return render(request, "accounts/register.html", context)


def registerReader(request):
    form = ContactForm()

    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            reader = Reader.objects.create(user=user)
            messages.success(request, "Conta criada com sucesso.")

            login(request, user)
            return redirect("books")

        else:
            messages.error(request, "Ocorreu um erro durante o registo")

    context = {
        "form": form
    }

    return render(request, "accounts/register.html", context)


@login_required(login_url="login")
def profile(request):
    user = request.user

    try:
        if request.user.reader:
            requisitions = Requisition.objects.filter(
                reader=user.reader, is_complete=True)

            context = {
                "requisitions": requisitions
            }

            return render(request, "accounts/user-profile.html", context)

    except ObjectDoesNotExist:
        pass

    return render(request, "accounts/user-profile.html")


@login_required(login_url="login")
def editProfile(request):
    user = request.user
    form = ProfileEditForm(instance=user)

    if request.method == "POST":
        form = ProfileEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("profile")

    context = {
        "form": form
    }

    return render(request, "accounts/profile-form.html", context)


def publicProfile(request, pk):
    user = Contact.objects.get(id=pk)

    context = {
        "user": user
    }

    return render(request, "accounts/profile.html", context)
