from django.contrib import admin
from . import models


@admin.register(models.Case)
class CaseAdmin(admin.ModelAdmin):

    search_fields = [
        "plaintiff_name",
        "defendant_name",
    ]
    ordering = ("court_datetime",)
    list_display = (
        "court_datetime",
        "plaintiff_name",
        "defendant_name",
        "court_location",
        "case_num",
        "case_name",
        "casedate_type",
        "case_attorney",
    )
