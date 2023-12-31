# Generated by Django 4.1.3 on 2023-07-16 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gimmeapi', '0003_product_image_url_user_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='order_id', to='gimmeapi.order')),
                ('product_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product_id', to='gimmeapi.product')),
            ],
        ),
    ]
