# Generated by Django 5.0.7 on 2024-08-24 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='payment_method',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
