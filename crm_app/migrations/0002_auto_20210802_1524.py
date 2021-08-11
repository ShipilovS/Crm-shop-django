# Generated by Django 3.2.5 on 2021-08-02 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='Название')),
                ('description', models.TextField(max_length=100, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]