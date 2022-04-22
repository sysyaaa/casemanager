from django.urls import path
from . import views

app_name = "cases"

urlpatterns = [
    path("", views.all_cases, name="all_cases"),
    path("<int:pk>/", views.case_detail, name="case_detail"),
    path("add/", views.case_add, name="case_add"),
    path("modify/<int:pk>/", views.case_modify, name="case_modify"),
    path("delete/<int:pk>/", views.case_delete, name="case_delete"),
]
