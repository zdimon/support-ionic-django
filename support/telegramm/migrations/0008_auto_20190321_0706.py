# Generated by Django 2.1.7 on 2019-03-21 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegramm', '0007_clienttelegramm_trello_board_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clienttelegramm',
            name='trello_board_name',
            field=models.CharField(blank=True, default='', max_length=250, null=True, verbose_name='Trello board'),
        ),
    ]
