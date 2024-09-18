# Generated by Django 5.1.1 on 2024-09-18 10:26

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productId',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
