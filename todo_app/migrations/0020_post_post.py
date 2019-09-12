# Generated by Django 2.2.5 on 2019-09-12 17:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0019_post_shared_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]