# Generated by Django 4.0.4 on 2022-05-02 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operatingsystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='versions',
            name='platforms',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
