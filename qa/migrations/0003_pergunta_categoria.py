# Generated by Django 5.1.1 on 2024-09-06 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0002_resposta'),
    ]

    operations = [
        migrations.AddField(
            model_name='pergunta',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='qa.categoria'),
        ),
    ]
