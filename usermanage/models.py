from django.db import models

# Create your models here.
class TUser(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45)
    userpwd = models.CharField(max_length=45)

    class Meta:
        db_table="TUser"

    def __str__(self):
        return self.username


class TextAdmin(models.Model):
    textadmin_id = models.AutoField(primary_key=True)
    textadmin_name = models.CharField(max_length=45)
    textadmin_pwd = models.CharField(max_length=45)

    class Meta:
        db_table="TextAdmin"

    def __str__(self):
        return self.textadmin_name

class TAdmin(models.Model):
    tadmin_id = models.AutoField(primary_key=True)
    tadmin_name = models.CharField(max_length=45)
    tadmin_pwd = models.CharField(max_length=45)

    class Meta:
        db_table="TAdmin"

    def __str__(self):
        return self.tadmin_name

class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=45)
    admin_pwd = models.CharField(max_length=45)

    class Meta:
        db_table="Admin"

    def __str__(self):
        return self.admin_name
