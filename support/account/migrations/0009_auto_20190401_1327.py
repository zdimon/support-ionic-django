# Generated by Django 2.1.7 on 2019-04-01 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20190327_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='trello_key',
            field=models.CharField(blank=True, default='864189665a3e2f50c5e8a59461082c267024968d646f1dcecb7a6238cebbc7b4', max_length=250, null=True, verbose_name='ключ в trello'),
        ),
        migrations.AlterField(
            model_name='client',
            name='trello_token',
            field=models.CharField(blank=True, default='1d980199101c6182074a15d587c4d008f00318337135dc7ce3f5c7ed784ffa03', max_length=250, null=True, verbose_name='токен в trello'),
        ),
    ]
