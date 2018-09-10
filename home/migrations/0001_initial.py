# Generated by Django 2.1.1 on 2018-09-10 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContratoSucursal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ContratoVuelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clase', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=150)),
                ('ciudad', models.CharField(max_length=150)),
                ('inTelefono', models.PositiveIntegerField()),
                ('telefono', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ImageHotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagenHotel', models.ImageField(blank=True, null=True, upload_to='fotos')),
            ],
        ),
        migrations.CreateModel(
            name='ImagePlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagenplan', models.ImageField(blank=True, null=True, upload_to='fotos')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('descripcion', models.TextField(max_length=500)),
                ('precio', models.PositiveIntegerField()),
                ('status', models.BooleanField(default=True)),
                ('imageplan', models.ManyToManyField(null=True, to='home.ImagePlan')),
            ],
        ),
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechallegada', models.DateField()),
                ('fechapartida', models.DateField()),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=250)),
                ('inTelefono', models.PositiveIntegerField()),
                ('telefono', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Turista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('apellido', models.CharField(max_length=150)),
                ('contratosucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ContratoSucursal')),
            ],
        ),
        migrations.CreateModel(
            name='Vuelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paisorigen', models.CharField(max_length=200)),
                ('ciudadorigen', models.CharField(max_length=200)),
                ('paisdestino', models.CharField(max_length=200)),
                ('ciudaddestino', models.CharField(max_length=200)),
                ('gate', models.CharField(default='', max_length=100)),
                ('group', models.PositiveSmallIntegerField()),
                ('seat', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='reservacion',
            name='turista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Turista'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='ImageHotel',
            field=models.ManyToManyField(null=True, to='home.ImageHotel'),
        ),
        migrations.AddField(
            model_name='contratovuelo',
            name='turista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Turista'),
        ),
        migrations.AddField(
            model_name='contratovuelo',
            name='vuelo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Vuelo'),
        ),
        migrations.AddField(
            model_name='contratosucursal',
            name='Sucursal',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.Sucursal'),
        ),
        migrations.AddField(
            model_name='contratosucursal',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Plan'),
        ),
    ]