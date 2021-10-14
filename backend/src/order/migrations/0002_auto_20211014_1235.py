# Generated by Django 3.2.5 on 2021-10-14 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='shipDistance',
        ),
        migrations.AddField(
            model_name='order',
            name='estimateDistance',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='shippingPrice',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
