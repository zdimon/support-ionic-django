# Generated by Django 2.1.7 on 2019-02-25 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worksection', '0006_auto_20190225_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wproject',
            name='page',
            field=models.CharField(db_index=True, max_length=250, unique=True, verbose_name='Страница в системе worksection'),
        ),
    ]
