from django.db import models
from core import models as core_models
from users import models as user_models


class Case(core_models.TimeStampedModel):

    """Case Model Definition"""

    COURT_LOACTION_CHOICES = [
        ("seoul", "서울"),
        ("busan", "부산"),
        ("daejeon", "대전"),
        ("daegu", "대구"),
    ]

    CASEDATE_TYPE = [
        ("arguedate", "변론기일"),
        ("crim_arguedate", "공판기일"),
        ("decisiondate", "선고기일"),
        ("settledate", "조정기일"),
        ("crim_arguedate", "공판기일"),
        ("questiondate", "심문기일"),
        ("etcdate", "기타"),
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

    def __str__(self):
        return f"{self.case_num} / {self. plaintiff_name} - {self.defendant_name}"
