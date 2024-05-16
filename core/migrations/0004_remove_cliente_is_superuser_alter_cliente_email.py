# Generated by Django 5.0.6 on 2024-05-16 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_cliente_delete_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='is_superuser',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True),
        ),
    ]