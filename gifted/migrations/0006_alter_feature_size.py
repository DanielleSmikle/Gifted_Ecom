# Generated by Django 4.1.5 on 2023-02-01 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifted', '0005_alter_feature_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='size',
            field=models.CharField(choices=[('small', 'SMALL'), ('large', 'LARGE')], default='small', max_length=6),
        ),
    ]