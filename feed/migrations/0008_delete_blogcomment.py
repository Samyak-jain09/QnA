# Generated by Django 4.0.1 on 2022-01-26 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_blogcomment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogComment',
        ),
    ]
