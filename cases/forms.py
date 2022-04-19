from django import forms
from django.forms import widgets
from .models import Case


class CaseAddForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = [
            "plaintiff_name",
            "defendant_name",
            "court_datetime",
            "court_location",
            "case_num",
            "case_name",
            "casedate_type",
            "case_attorney",
            "memo",
        ]
        # widgets = {
        #     "plaintiff_name": forms.TextInput(attrs={"class": "form-control"}),
        #     "defendant_name": forms.TextInput(attrs={"class": "form-control"}),
        #     "court_datetime": widgets.DateTimeInput(
        #         attrs={"type": "datetime-local", "class": "form-control"}
        #     ),
        #     "court_location": forms.Select(attrs={"class": "form-select"}),
        #     "case_num": forms.TextInput(
        #         attrs={"class": "form-control", "placeholder": "예: 2000가합1234"}
        #     ),
        #     "case_name": forms.TextInput(attrs={"class": "form-control"}),
        #     "casedate_type": forms.Select(attrs={"class": "form-select"}),
        #     "case_attorney": forms.Select(attrs={"class": "form-select"}),
        #     "memo": forms.Textarea(attrs={"class": "form-control", "rows": 10}),
        # }
