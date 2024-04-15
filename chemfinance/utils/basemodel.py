from django.db import models
import uuid 
from django.core.validators import RegexValidator


validate_comcode = RegexValidator(
    regex='[a-zA-Z0-9]$',
    message='Field cannot contain special characters',
    code='invalid_name'
)




# Create your models here.
class CommonFields(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    gcode= models.CharField(max_length = 50, verbose_name="Group Code", validators=[validate_comcode])
    comcode= models.CharField(max_length = 50, verbose_name="Company Code", validators=[validate_comcode])
    brcode= models.CharField(max_length = 50, verbose_name="Branch Code", validators=[validate_comcode])
    ucode = models.CharField(max_length = 50, verbose_name="User Code", validators=[validate_comcode])
    trdate = models.DateTimeField(auto_now_add = True,verbose_name="Transation Date")
    description = models.TextField(blank= True)
    class Meta:
        abstract = True

