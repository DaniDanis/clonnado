# Generated by Django 4.0.6 on 2022-07-26 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_alter_profile_foto_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birt_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
