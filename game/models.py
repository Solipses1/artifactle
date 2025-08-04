from django.db import models

# Create your models here.
class Museum(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    website = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"

class Country(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=128)
    latitude = models.CharField(max_length=128)
    longitude = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"

class Artifact(models.Model):
    name = models.CharField(max_length=128)
    year = models.CharField(max_length=128)
    description = models.TextField()
    materials = models.CharField(max_length=128)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="artifacts_country")
    museum = models.ForeignKey(Museum, on_delete=models.CASCADE, related_name="artifacts_museum")
    artist = models.CharField(max_length=128)
    image = models.ImageField(upload_to="media")
    
    def __str__(self):
        return f"{self.name}"

class Game(models.Model):
    date = models.DateField()
    round_1 = models.ForeignKey(Artifact, on_delete=models.CASCADE, unique=True, related_name="round_1_artifact")
    round_2 = models.ForeignKey(Artifact, on_delete=models.CASCADE, unique=True, related_name="round_2_artifact")
    round_3 = models.ForeignKey(Artifact, on_delete=models.CASCADE, unique=True, related_name="round_3_artifact")
    
    def __str__(self):
        return f"Game {self.id}"