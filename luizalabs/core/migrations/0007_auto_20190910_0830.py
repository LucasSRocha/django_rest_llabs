# Generated by Django 2.1.12 on 2019-09-10 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190910_0650'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermagalu',
            old_name='name',
            new_name='username',
        ),
        migrations.AddField(
            model_name='usermagalu',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='usermagalu',
            name='password',
            field=models.CharField(default='', max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]