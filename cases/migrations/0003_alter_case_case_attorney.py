# Generated by Django 4.0.3 on 2022-03-23 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cases', '0002_case_memo_alter_case_court_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='case_attorney',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='담당변호사'),
        ),
    ]