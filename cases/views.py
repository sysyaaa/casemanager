from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import CaseAddForm
from .models import Case


def all_cases(request):

    """사건 목록 출력"""
    if not request.user.is_authenticated:
        return redirect("users:login")
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
    if not request.user.is_authenticated:
        return redirect("users:login")
    else:
        data = get_object_or_404(Case, pk=pk)
        context = {"data": data}
        print(data.court_datetime)
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


@login_required(login_url="users:login")
def case_modify(request, pk):
    """사건 수정"""
    case = get_object_or_404(Case, pk=pk)
    if request.method == "POST":
        form = CaseAddForm(request.POST, instance=case)
        if form.is_valid():
            case = form.save(commit=False)
            case.modify_date = timezone.now()
            case.save()
            return redirect("cases:all_cases")
    else:
        form = CaseAddForm(instance=case)
    context = {"form": form}
    return render(request, "cases/case_modify.html", context)


@login_required(login_url="users:login")
def case_delete(request, pk):
    """사건 삭제"""
    case = get_object_or_404(Case, pk=pk)
    case.delete()
    return redirect("cases:all_cases")
