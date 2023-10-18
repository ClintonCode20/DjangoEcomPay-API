# Generated by Django 4.0.5 on 2023-10-07 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pending_status',
            field=models.CharField(choices=[('P', 'Pending'), ('C', 'Complete'), ('F', 'Failed')], default='P', max_length=50),
        ),
    ]
