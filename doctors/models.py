from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    photo = models.CharField(max_length=60)
    phone = models.CharField(max_length=20)
    nid = models.CharField(max_length=30)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=160)
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

