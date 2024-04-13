from django.db import models
import uuid 

# Create your models here.
class CommonFields(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    gcode= models.CharField(max_length = 50, verbose_name="Group Code")
    comcode= models.CharField(max_length = 50, verbose_name="Company Code")
    brcode= models.CharField(max_length = 50, verbose_name="Branch Code")
    ucode = models.CharField(max_length = 50, verbose_name="User Code")
    trdate = models.DateTimeField(auto_now_add = True,verbose_name="Transation Date")
    description = models.TextField(blank= True)
    class Meta:
        abstract = True

