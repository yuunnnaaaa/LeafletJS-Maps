from django.db import models

class ServiceArea(models.Model):
    name = models.CharField(max_length=100, help_text="Nama area layanan")
    description = models.TextField(blank=True, null=True, help_text="Deskripsi singkat area layanan")
    latitude = models.FloatField(help_text="Koordinat latitude titik pemancar")
    longitude = models.FloatField(help_text="Koordinat longitude titik pemancar")
    coverage_radius_km = models.FloatField(default=1.0, help_text="Radius jangkauan sinyal (km)")

    def __str__(self):
        return self.name
    

