# Generated by Django 4.2.6 on 2024-04-24 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_skin_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='money',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
