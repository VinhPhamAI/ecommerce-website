# Generated by Django 5.0.7 on 2024-08-18 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
