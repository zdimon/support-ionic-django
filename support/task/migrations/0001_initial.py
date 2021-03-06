# Generated by Django 2.1.7 on 2019-03-21 08:03

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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='files')),
                ('content', models.TextField(blank=True, max_length=150, null=True, verbose_name='Содержание')),
                ('author', models.TextField(blank=True, max_length=250, null=True, verbose_name='Автор')),
                ('avatar', models.TextField(blank=True, max_length=250, null=True, verbose_name='Аватар')),
                ('file_url', models.TextField(blank=True, max_length=250, null=True, verbose_name='Ссылка на файл')),
                ('file_url_orig', models.TextField(blank=True, max_length=250, null=True, verbose_name='Ссылка на превью')),
                ('is_ws_exported', models.BooleanField(default=False, verbose_name='Is WS exported?')),
                ('ws_id', models.CharField(default='', max_length=250, verbose_name='WS ID')),
                ('is_trello_exported', models.BooleanField(default=False, verbose_name='Is trello exported?')),
                ('is_file', models.BooleanField(default=False, verbose_name='Is file?')),
                ('trello_id', models.CharField(blank=True, default='', max_length=250, null=True, verbose_name='Trello ID')),
                ('is_support', models.BooleanField(default=False, verbose_name='суппорт')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='task.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('contacts', models.TextField(verbose_name='Контакты')),
                ('status', models.CharField(default='В процессе рассмотрения', max_length=100, verbose_name='Статус')),
                ('trello_board_name', models.CharField(blank=True, db_index=True, default='', max_length=250, null=True, verbose_name='Trello board')),
                ('telegramm_room', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='telegramm chat_id')),
                ('is_from_telegramm', models.BooleanField(default=False, verbose_name='Is from telegramm?')),
                ('is_done_from_telegramm', models.BooleanField(default=False, verbose_name='Is done from telegramm?')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is active?')),
                ('source', models.CharField(default='', max_length=250, verbose_name='Источник')),
                ('is_ws_exported', models.BooleanField(default=False, verbose_name='Is WS exported?')),
                ('ws_link', models.CharField(default='', max_length=250, verbose_name='WS link')),
                ('is_trello_exported', models.BooleanField(default=False, verbose_name='Is WS exported?')),
                ('trello_link', models.CharField(blank=True, default='', max_length=250, null=True, verbose_name='Trello link')),
                ('trello_id', models.CharField(blank=True, db_index=True, default='', max_length=250, null=True, verbose_name='Trello id')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is deleted?')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='task.Category')),
                ('subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='task.SubCategory')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='task.Task'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
