# Generated by Django 2.2.5 on 2019-09-11 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0015_addlist_add_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addlist',
            name='list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addlist', to='todo_app.Post'),
        ),
    ]