# Generated by Django 3.0.8 on 2020-07-15 04:39

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pst',
            new_name='Post',
        ),
    ]
