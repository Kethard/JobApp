# Generated by Django 4.2.6 on 2023-11-16 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribe',
            name='option',
            field=models.CharField(choices=[('W', 'Weekly'), ('M', 'Monthly')], default='NULL', max_length=2),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
