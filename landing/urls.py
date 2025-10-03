from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("submit-scoping-call/", views.submit_scoping_call, name="submit_scoping_call"),
    path("submit-brief/", views.submit_brief, name="submit_brief"),
    path("submit-contact/", views.submit_contact, name="submit_contact"),
]