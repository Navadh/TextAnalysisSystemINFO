from django.db import models

# import os,django
#
# os.environ.setdefault("DJANGO_SETTING_MODULE", "TextAnalysisSystem3.settings")
# django.setup()
# Create your models here.


class TextMange(models.Model):
    ttextmanageid=models.AutoField(primary_key=True)
    # userid = models.ForeignKey('usermanage.TUser', on_delete=models.CASCADE, db_column='userid')
    userid = models.IntegerField()
    updatetime=models.DateTimeField()
    ptype=models.CharField(max_length=45)
    pname=models.CharField(max_length=45)

    class Meta:
        db_table="TTextManage"






