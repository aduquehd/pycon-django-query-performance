from django.db import models
from django.utils import timezone


class Owner(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class PetType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Pet(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    type = models.ForeignKey(PetType, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name


class PetOwner(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)


class Revision(models.Model):
    client = models.ForeignKey(Owner, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)


class RevisionNotes(models.Model):
    revision = models.ForeignKey(Revision, on_delete=models.CASCADE)
    notes = models.TextField()
