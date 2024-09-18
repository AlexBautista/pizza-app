# Generated by Django 5.1.1 on 2024-09-17 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_rename_pizzas_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pizza_flavor',
            field=models.CharField(choices=[('Pepperoni', 'Pepperoni'), ('Supreme', 'Supreme'), ('Chicago', 'Chicago')], default='Pepperoni', max_length=20),
        ),
    ]