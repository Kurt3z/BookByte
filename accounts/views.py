from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from .models import Contact, Reader
from .forms import ContactForm


def loginUser(request):
    if request.user.is_authenticated:
        return redirect("books")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print(username, password)

        try:
            user = Contact.objects.get(username=username)
        except:
            messages.error(request, "Nome de utilizador não existente.")
            return render(request, "accounts/login.html")

        if user is not None:
            login(request, user)
            messages.success(request, "Sessão iniciada com sucesso")
            return redirect("books")
        else:
            messages.error(
                request, "Nome de utilizador ou palavra-passe incorretos.")

    return render(request, "accounts/login.html")


def registerReader(request):
    form = ContactForm()

    if request.user.is_authenticated:
        return redirect("books")

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
