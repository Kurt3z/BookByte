from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from accounts.models import Contact


def loginUser(request):
    page = "login"
    context = {
        "page": page
    }

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
            return render(request, "accounts/login.html", context)

        if user is not None:
            login(request, user)
            messages.success(request, "Sessão iniciada com sucesso")
            return redirect("books")
        else:
            messages.error(
                request, "Nome de utilizador ou palavra-passe incorretos.")

    return render(request, "accounts/login.html", context)


def registerReader(request):
    pass
