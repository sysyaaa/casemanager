from django.db import models
from core import models as core_models
from users import models as user_models


class Case(core_models.TimeStampedModel):

    """Case Model Definition"""

    COURT_LOACTION_CHOICES = [
        ("서울", "서울"),
        ("부산", "부산"),
        ("대전", "대전"),
        ("대구", "대구"),
    ]

    CASEDATE_TYPE = [
        ("변론기일", "변론기일"),
        ("공판기일", "공판기일"),
        ("선고기일", "선고기일"),
        ("조정기일", "조정기일"),
        ("공판기일", "공판기일"),
        ("심문기일", "심문기일"),
        ("기타", "기타"),
    ]

    plaintiff_name = models.CharField(max_length=50, verbose_name="원고", blank=True)
    defendant_name = models.CharField(max_length=50, verbose_name="피고", blank=True)
    court_datetime = models.DateTimeField(verbose_name="다음 기일", blank=True)
    court_location = models.CharField(
        max_length=20, choices=COURT_LOACTION_CHOICES, verbose_name="관할", blank=True
    )
    case_num = models.CharField(max_length=20, verbose_name="사건번호", blank=True)
    case_name = models.CharField(max_length=20, verbose_name="사건명", blank=True)
    casedate_type = models.CharField(
        max_length=20, choices=CASEDATE_TYPE, verbose_name="기일구분"
    )
    case_attorney = models.ForeignKey(
        user_models.User, on_delete=models.CASCADE, verbose_name="담당변호사", null=True
    )
    memo = models.TextField(verbose_name="메모", blank=True)

    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.case_num} / {self. plaintiff_name} - {self.defendant_name}"
