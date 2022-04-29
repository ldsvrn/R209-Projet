from django.db import models

# Create your models here.
class operatingsystem(models.Model):
    name = models.CharField(max_length = 100) 
    developer = models.CharField(max_length = 100)
    software_license = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return f"{self.name} developpé par {self.developer} avec une license {self.software_license}"


class versions(models.Model):
    operating_system = models.ForeignKey(operatingsystem, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100) 
    release_date = models.DateField(blank=True, null = True)
    platforms = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return f"{self.name} paru le {self.release_date} supporte {self.platforms}"

