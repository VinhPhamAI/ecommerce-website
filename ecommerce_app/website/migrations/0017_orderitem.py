# Generated by Django 5.0.7 on 2024-08-21 10:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_alter_profile_book_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('ordered_at', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_items', to='website.book')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='website.profile')),
            ],
        ),
    ]
