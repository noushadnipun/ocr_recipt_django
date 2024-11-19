from django.db import models

# Create your models here.
class Receipt(models.Model):
    image = models.ImageField(upload_to='receipts/')
    extracted_data = models.JSONField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)