# Generated by Django 3.1.7 on 2021-03-26 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=6),
            preserve_default=False,
        ),
    ]