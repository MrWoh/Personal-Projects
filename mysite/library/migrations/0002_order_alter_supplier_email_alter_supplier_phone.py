# Generated by Django 4.0.5 on 2022-06-29 08:13

from django.db import migrations, models
import library.models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(max_length=50, verbose_name='Uzsakymas')),
                ('amount', models.FloatField(max_length=5, verbose_name='Kiekis')),
                ('unit', models.CharField(blank=True, choices=[('a', 'Vnt'), ('b', 'Kg'), ('c', 'G'), ('d', 'L')], default='a', help_text='Matas', max_length=1)),
                ('note', models.CharField(max_length=100, verbose_name='Aprasymas')),
            ],
        ),
        migrations.AlterField(
            model_name='supplier',
            name='email',
            field=models.EmailField(default=library.models.default_mail, help_text='Iveskite tiekejo elektronini pasta', max_length=50, verbose_name='Elektroninis pastas'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='phone',
            field=models.CharField(default=library.models.default_number, help_text='Iveskite tiekejo Telefono numeri', max_length=50, verbose_name='Telefono numeris'),
        ),
    ]
