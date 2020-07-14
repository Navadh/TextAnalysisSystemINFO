from django.db import models

# Create your models here.


class TextMange(models.Model):
    ttextmanageid=models.AutoField(primary_key=True)
    userid = models.IntegerField()
    updatetime=models.DateTimeField()
    ptype=models.CharField(max_length=45)
    pname=models.CharField(max_length=45)


    class Meta:
        db_table="TTextManage"
