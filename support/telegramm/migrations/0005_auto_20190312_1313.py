# Generated by Django 2.1.7 on 2019-03-12 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegramm', '0004_clienttelegramm_is_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clienttelegramm',
            name='login',
            field=models.CharField(blank=True, db_index=True, max_length=150, null=True, verbose_name='Логин в telegramm'),
        ),
    ]
