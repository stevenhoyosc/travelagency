# Generated by Django 2.1.1 on 2018-09-18 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180918_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contratovuelo',
            name='vuelo',
            field=models.ManyToManyField(blank=True, null=True, to='home.Vuelo'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='ImageHotel',
            field=models.ManyToManyField(blank=True, null=True, to='home.ImageHotel'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='imageplan',
            field=models.ManyToManyField(blank=True, null=True, to='home.ImagePlan'),
        ),
    ]
