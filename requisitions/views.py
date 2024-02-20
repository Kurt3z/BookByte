from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse, HttpResponse
import json
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Requisition
from models.models import Content


def is_reader(user):
    return hasattr(user, "reader")


def requisitions(request):
    pass


def requisition(request, pk):
    requisition = Requisition.objects.get(id=pk)
    context = {
        "requisition": requisition
    }

    return render(request, "requisitions/requisition-detail.html", context)


@login_required(login_url="login")
def requisitionCart(request):
    if is_reader(request.user):
        reader = request.user.reader
        requisition, created = Requisition.objects.get_or_create(
            reader=reader, is_complete=False)
        contents = requisition.contents.all()

        context = {
            "contents": contents,
            "requisition": requisition
        }
        return render(request, "requisitions/requisition-cart.html", context)
    else:
        return redirect("profile")


def updateContent(request):
    data = json.loads(request.body)
    contentId = data["contentId"]
    action = data["action"]

    print("Action: ", action)
    print("contentId: ", contentId)

    content = Content.objects.get(id=contentId)

    if content.quantity == 0:
        return JsonResponse({"error": "Item fora de stock."}, status=400)

    reader = request.user.reader

    requisition, created = Requisition.objects.get_or_create(
        reader=reader, is_complete=False)

    if content in requisition.contents.all() and action == "add":
        return JsonResponse({"error": "Item já presente na sua requisição. Só pode requisitar um item de cada."}, status=400)

    if action == "add":
        requisition.contents.add(content)
    elif action == "remove":
        requisition.contents.remove(content)

    return JsonResponse('Content was added', safe=False)


def submitRequisition(request, pk):
    requisition = Requisition.objects.get(id=pk)
    requisition.submit_requisition()

    for content in requisition.contents.all():
        content.quantity -= 1
        content.save()

    target_url = reverse("requisition", kwargs={"pk": pk})

    return redirect(target_url)


def getRequisitionItemCount(request):
    reader = request.user.reader
    requisition = Requisition.objects.filter(
        reader=reader, is_complete=False).first()

    if requisition:
        item_count = requisition.contents.count()
        return JsonResponse({"item_count": item_count})

    return JsonResponse({"item_count": 0})
