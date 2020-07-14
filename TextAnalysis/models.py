from django.db import models
from TextManage.models import TextMange

class WFreq(models.Model):
    ttextmanageid = models.ForeignKey(TextMange, on_delete=models.CASCADE)
    wordid = models.AutoField(primary_key=True)
    word = models.CharField(max_length=45,null=False)
    frequency = models.CharField(max_length=5,null=False)

    class Meta:
        db_table='wfreq'
