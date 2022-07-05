from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from datetime import date
# functions


def default_mail():
    return 'mail@mail.com'


def default_number():
    return '+3706'

# Models


class Supplier(models.Model):
    supplier = models.CharField('Tiekėjas', max_length=200,
                                help_text='Įveskite tiekejo pavadinimą')
    email = models.EmailField('Elektroninis pastas', max_length=50, default=default_mail,
                              help_text='Iveskite tiekejo elektronini pasta')
    phone = models.CharField('Telefono numeris', max_length=50, default=default_number,
                             help_text='Iveskite tiekejo Telefono numeri')

    def __str__(self):
        return self.supplier


class Categories(models.Model):
    category = models.CharField(
        'Kategorija', max_length=50)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category


class Order(models.Model):
    UNIT_CHOICE = (
        ('a', 'Vnt'),
        ('b', 'Kg'),
        ('c', 'G'),
        ('d', 'L'),
    )

    """Uzsakymo pildymas"""
    supplier = models.ForeignKey(
        'Supplier', on_delete=models.SET_NULL, null=True, related_name="orders")
    order = models.CharField('Uzsakymas', max_length=50)
    amount = models.FloatField('Kiekis', max_length=5)
    unit = models.CharField(
        'Mato Vienetas',
        max_length=1,
        choices=UNIT_CHOICE,
        blank=True,
        default='a',
    )
    order_code = models.CharField('Kodas', blank=True, max_length=20)
    note = models.CharField(
        'Aprasymas', blank=True, max_length=50)
    category = models.ManyToManyField(
        'Categories', help_text='Priskirkite kategorijai')

    def __str__(self):
        return '{}. Kiekis: {} {}.    {}.  "{}"'.format(self.order,
                                                        self.amount,
                                                        self.get_unit_display(),
                                                        self.order_code,
                                                        self.note
                                                        )
