# Generated by Django 2.1.7 on 2019-04-01 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_auto_20190328_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('new', 'В процессе рассмотрения'), ('inprocess', 'В работе'), ('done', 'Выполнен')], default='new', max_length=100, verbose_name='Статус'),
        ),
    ]
