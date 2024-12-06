# Generated by Django 4.2.16 on 2024-12-05 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=100)),
                ('valoracion', models.IntegerField()),
            ],
            options={
                'permissions': [('development', 'Permiso como Desarrollador'), ('scrum_master', 'Permiso como Scrum Master'), ('product_owner', 'Permiso como Product Owner')],
            },
        ),
    ]
