# Generated by Django 4.2.10 on 2024-02-19 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_menuitem_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='position',
            field=models.DecimalField(decimal_places=1, max_digits=100, verbose_name='Позиция'),
        ),
    ]