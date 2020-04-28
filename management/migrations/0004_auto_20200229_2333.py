# Generated by Django 3.0.3 on 2020-02-29 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_auto_20200228_1256'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='type',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='product',
            name='types',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='management.Type', verbose_name='Categories'),
        ),
    ]