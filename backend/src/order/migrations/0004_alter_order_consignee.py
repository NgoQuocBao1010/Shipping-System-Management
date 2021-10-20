# Generated by Django 3.2.5 on 2021-10-20 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_profile_user'),
        ('order', '0003_alter_order_consignee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='consignee',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order', to='account.profile'),
        ),
    ]
