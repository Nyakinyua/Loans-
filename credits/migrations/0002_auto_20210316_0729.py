# Generated by Django 3.0 on 2021-03-16 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='loanAmount',
        ),
        migrations.AddField(
            model_name='loan',
            name='ProductId',
            field=models.CharField(default='L01', max_length=10),
        ),
    ]