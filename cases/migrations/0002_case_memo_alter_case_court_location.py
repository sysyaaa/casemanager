# Generated by Django 4.0.3 on 2022-03-23 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='memo',
            field=models.TextField(blank=True, verbose_name='메모'),
        ),
        migrations.AlterField(
            model_name='case',
            name='court_location',
            field=models.CharField(blank=True, choices=[('seoul', '서울'), ('busan', '부산'), ('daejeon', '대전'), ('daegu', '대구')], max_length=20, verbose_name='관할'),
        ),
    ]
