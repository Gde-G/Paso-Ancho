# Generated by Django 4.1.1 on 2022-09-13 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulta',
            name='amount_adults',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='consulta',
            name='amount_kids',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='consulta',
            name='date_from',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='consulta',
            name='date_to',
            field=models.DateField(blank=True, null=True),
        ),
    ]
