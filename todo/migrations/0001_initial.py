# Generated by Django 3.2.3 on 2021-05-23 06:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255, verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Todo Category',
                'verbose_name_plural': 'Todos Categories',
            },
        ),
        migrations.CreateModel(
            name='TodoPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_title', models.CharField(max_length=255, verbose_name='Title')),
                ('todo_description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('todo_created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('todo_updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('todo_favorite', models.BooleanField(default='False', verbose_name='Favorite')),
                ('todo_completed', models.BooleanField(default='False', verbose_name='Completed')),
                ('todo_status', models.CharField(choices=[('draft', 'Private'), ('published', 'Public')], default='draft', max_length=12, verbose_name='Status')),
                ('todo_author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('todo_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.todocategory', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Todo',
                'verbose_name_plural': 'Todos',
                'ordering': ('todo_created',),
            },
        ),
    ]
