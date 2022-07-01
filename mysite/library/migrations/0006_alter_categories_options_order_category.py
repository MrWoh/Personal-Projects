# Generated by Django 4.0.5 on 2022-06-30 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_order_supplier'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Kategorija', 'verbose_name_plural': 'Kategorijos'},
        ),
        migrations.AddField(
            model_name='order',
            name='category',
            field=models.ManyToManyField(help_text='Priskirkite kategorijai', to='library.categories'),
        ),
    ]
