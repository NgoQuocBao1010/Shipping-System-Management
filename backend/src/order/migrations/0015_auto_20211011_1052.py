# Generated by Django 3.2.5 on 2021-10-11 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='paymentMethod',
            field=models.IntegerField(choices=[(1, 'Pay by consignor'), (2, 'Pay by consignee')], null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='productPreview',
            field=models.IntegerField(choices=[(1, 'Customer not allow to observe products'), (2, 'Customer allow to observe products but not to try them'), (3, 'Customer allow to try products')], null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='shippingType',
            field=models.IntegerField(choices=[(1, 'Standard'), (2, 'Advanced')], null=True),
        ),
    ]