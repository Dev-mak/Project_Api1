from django.db import models


# Create your models here.
class Detail(models.Model):
    Roll_Number = models.CharField(verbose_name='Roll_No', max_length=255, null=False, unique=True)
    name = models.CharField(verbose_name="name", max_length=225, null=False)
    DOB = models.CharField(verbose_name="DOB", max_length=225, null=False)

    def __str__(self):
        return self.name

class Mark(models.Model):
    student = models.ForeignKey(to=Detail, on_delete=models.CASCADE)
    mark = models.IntegerField(verbose_name="Mark", null=False)

    def __str__(self):
        return str(self.student)

# Create your models here.
