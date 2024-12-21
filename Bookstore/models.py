from django.db import models


class Books(models.Model):

    book_name = models.CharField(max_length=255)
    book_price = models.CharField(max_length=255)
    book_author = models.CharField(max_length=255,default="Author")
    book_image = models.ImageField(null='True',blank='True',upload_to="images/")
    book_details=models.CharField(max_length=255)
    banner = models.ImageField(null=True,default='books.jpg',blank=True,upload_to="images/")
    class Meta:
        db_table = "book_store"

class Login(models.Model):
    user_name = models.CharField(max_length=255)
    user_pwd = models.CharField(max_length=50)
    class Meta:
        db_table = "login_table"


class Register(models.Model):
    full_name = models.CharField(default= 'ABC',max_length=255)
    user_name = models.CharField(max_length=255)
    user_pwd = models.CharField(max_length=50)
    user_id = models.EmailField(max_length=100,unique=True)

    class Meta:
        db_table = "register_table"