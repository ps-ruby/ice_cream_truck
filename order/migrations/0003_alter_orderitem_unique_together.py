# Generated by Django 4.0.3 on 2022-04-10 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_items', '0006_alter_fooditem_quantity'),
        ('order', '0002_alter_orderitem_quantity'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='orderitem',
            unique_together={('order', 'food_item')},
        ),
    ]