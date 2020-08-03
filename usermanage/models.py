from django.db import models

# Create your models here.


class TUser(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45)
    userpwd = models.CharField(max_length=45)

    class Meta:
        db_table = "TUser"

    def __str__(self):
        return self.username


class TextAdmin(models.Model):
    TextAdmin_userid = models.AutoField(primary_key=True)
    TextAdmin_username = models.CharField(max_length=50)
    TextAdmin_pwd = models.CharField(max_length=50)

    class Meta:
        db_table = "TextAdmin"

    def __str__(self):
        return self.TextAdmin_username
