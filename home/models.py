from django.db import models

# Create your models here.
class ImagePlan(models.Model):
    imagenplan         = models.ImageField(upload_to ='fotos',null =True,blank = True)

   

class ImageHotel(models.Model):
    imagenHotel        = models.ImageField(upload_to ='fotos', null =True,blank = True)
    
    

class Plan(models.Model):
    nombre             = models.CharField(max_length = 250)
    descripcion        = models.TextField(max_length = 500)
    precio             = models.PositiveIntegerField()
    status             = models.BooleanField(default=True)
    imageplan          = models.ManyToManyField(ImagePlan, null = True)

    def __str__(self):
        return self.nombre

class Sucursal(models.Model):
    direccion          = models.CharField(max_length = 250)
    inTelefono         = models.PositiveIntegerField()
    telefono           = models.PositiveIntegerField()

    def __str__(self):
        return self.direccion

class ContratoSucursal(models.Model):
    detalle            = models.TextField(max_length= 500)
    plan               = models.ForeignKey(Plan, on_delete=models.CASCADE)
    Sucursal           = models.OneToOneField(Sucursal, on_delete=models.CASCADE)

    def __str__(self):
        return self.detalle

class Turista(models.Model):
    nombre             = models.CharField(max_length = 150)
    apellido           = models.CharField(max_length = 150)
    contratosucursal   = models.ForeignKey(ContratoSucursal, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre

class Vuelo(models.Model):
    paisorigen         = models.CharField(max_length = 200)
    ciudadorigen       = models.CharField(max_length = 200)
    paisdestino        = models.CharField(max_length = 200)
    ciudaddestino      = models.CharField(max_length = 200)
    gate               = models.CharField(max_length = 100, default = '')
    group              = models.PositiveSmallIntegerField()
    seat               = models.CharField(max_length = 100)

    fecha              = models.DateField()
    hora               = models.TimeField()

    def __str__(self):
        return self.paisorigen

class ContratoVuelo(models.Model):
    clase              = models.CharField(max_length = 150)
    turista            = models.ForeignKey(Turista, on_delete=models.CASCADE)
    vuelo              = models.ForeignKey(Vuelo, on_delete=models.CASCADE)

    def __str__(self):
        return self.clase

class Hotel(models.Model):
    nombre             = models.CharField( max_length = 150 )
    direccion          = models.CharField( max_length = 150 )
    ciudad             = models.CharField( max_length = 150 )
    inTelefono         = models.PositiveIntegerField()
    telefono           = models.PositiveIntegerField()
    ImageHotel         = models.ManyToManyField(ImageHotel, null = True)

    def __str__(self):
        return self.nombre

class Reservacion(models.Model):
    fechallegada       = models.DateField()
    fechapartida       = models.DateField()
    turista            = models.ForeignKey(Turista, on_delete = models.CASCADE)
    hotel              = models.ForeignKey(Hotel, on_delete = models.CASCADE)
