# Generated by Django 5.0.3 on 2024-04-24 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_alter_images_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
