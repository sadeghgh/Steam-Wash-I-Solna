from django.db import models

# Create your models here.


class CarModel(models.Model):
    name_car = models.CharField(max_length=50)
    image = models.ImageField(default='', upload_to='store_image/', null=True)

    def __str__(self):
        return self.name_car


class SelectionServices(models.Model):
    name_car = models.CharField(max_length=50)
    discription = models.TextField()
    discription_pack = models.TextField()
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.discription


class RequestUser(models.Model):
    author = models.CharField(max_length=50)
    name_car = models.CharField(max_length=50)
    discription_service = models.TextField()
    price = models.CharField(max_length=50)
    lat = models.CharField(max_length=150)
    lng = models.CharField(max_length=150)
    timedate = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    car_tag = models.CharField(max_length=150)
    payment_type = models.CharField(max_length=50)
    doit = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author


class Comment(models.Model):
    author = models.CharField(max_length=50)
    satisfaction = models.TextField()

    def __str__(self):
        return self.satisfaction


class DeleteRequest(models.Model):
    author = models.CharField(max_length=50)
    discription_service = models.TextField()
    count = models.CharField(max_length=50)

    def __str__(self):
        return self.author


class DiscountCode(models.Model):
    user = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    counter = models.CharField(max_length=50)
    orders = models.CharField(max_length=50)

    def __str__(self):
        return self.user
