from django.urls import path

from . import views


urlpatterns = [
    path("requisitions/", views.requisitions, name="requisitions"),
    path("requisition/<str:pk>/", views.requisition, name="requisition"),


    path("requisition-cart/",
         views.requisitionCart, name="requisition-cart"),
    path("update-content/", views.updateContent, name="update-content"),
    path("get-requisition-item-count/", views.getRequisitionItemCount,
         name="get_requisition_item_count"),
    path("submit-requisition/<str:pk>/",
         views.submitRequisition, name="submit-requisition")
]
