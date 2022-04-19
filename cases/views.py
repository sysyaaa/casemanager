from django.shortcuts import render, get_object_or_404, redirect
from .forms import CaseAddForm
from .models import Case


def all_cases(request):

    """사건 목록 출력"""
    if not request.user.is_authenticated:
        data = {
            "username": request.user,
            "is_authenticated": request.user.is_authenticated,
        }
    else:
        data = {
            "last_login": request.user.last_login,
            "username": request.user.username,
            "password": request.user.password,
            "is_authenticated": request.user.is_authenticated,
            "case_list": Case.objects.order_by("court_datetime"),
        }
    context = {"data": data}
    return render(request, "cases/case_list.html", context)


def case_detail(request, pk):
    """사건 내용 출력"""
    data = get_object_or_404(Case, pk=pk)
    context = {"data": data}
    return render(request, "cases/case_detail.html", context)


def case_add(request):
    """사건 추가"""

    if request.method == "POST":
        form = CaseAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cases:all_cases")
    else:
        form = CaseAddForm()

    return render(request, "cases/case_add.html", {"form": form})
