# Generated by Django 4.1.5 on 2023-01-23 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifted', '0002_alter_feature_options_remove_feature_size_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='size',
            field=models.CharField(choices=[('small', 'SMALL'), ('large', 'LARGE')], default='small', max_length=5),
        ),
    ]
