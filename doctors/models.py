from django.contrib.auth.models import User
from django.db import models


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    photo = models.CharField(max_length=60)
    phone = models.CharField(max_length=20)
    nid = models.CharField(max_length=30)
    nid_photo = models.CharField(max_length=30)
    bmdc = models.CharField(max_length=30)
    bmdc_photo = models.CharField(max_length=30)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Doctors'


class TreatmentCategory(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Treatment Categories'


class Treatment(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(TreatmentCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Treatments'


class Chamber(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Chambers'


class ChamberDoctor(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    chamber = models.ForeignKey(Chamber, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ChamberPhoto(models.Model):
    photo = models.CharField(max_length=60)
    chamber = models.ForeignKey(Chamber, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ChamberTreatment(models.Model):
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    chamber = models.ForeignKey(Chamber, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Chamber Treatments'
