# Generated by Django 3.1.2 on 2020-12-05 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_car', models.CharField(max_length=50)),
                ('image', models.ImageField(default='', null=True, upload_to='store_image/')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('satisfaction', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DeleteRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('discription_service', models.TextField()),
                ('count', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DiscountCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=50)),
                ('counter', models.CharField(max_length=50)),
                ('orders', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RequestUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('name_car', models.CharField(max_length=50)),
                ('discription_service', models.TextField()),
                ('price', models.CharField(max_length=50)),
                ('lat', models.CharField(max_length=150)),
                ('lng', models.CharField(max_length=150)),
                ('timedate', models.CharField(max_length=150)),
                ('model', models.CharField(max_length=150)),
                ('color', models.CharField(max_length=150)),
                ('car_tag', models.CharField(max_length=150)),
                ('payment_type', models.CharField(max_length=50)),
                ('doit', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SelectionServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_car', models.CharField(max_length=50)),
                ('discription', models.TextField()),
                ('discription_pack', models.TextField()),
                ('price', models.CharField(max_length=50)),
            ],
        ),
    ]