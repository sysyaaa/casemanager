from django.urls import path
from . import views

app_name = "cases"

urlpatterns = [
    path("", views.all_cases, name="all_cases"),
    path("<int:pk>/", views.detail, name="case_detail"),
]
