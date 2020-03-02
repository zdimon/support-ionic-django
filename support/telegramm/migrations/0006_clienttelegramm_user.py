# Generated by Django 2.1.7 on 2019-03-14 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('telegramm', '0005_auto_20190312_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='clienttelegramm',
            name='user',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
    ]
