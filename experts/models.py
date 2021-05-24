import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class ExpertProfile(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='expert_profile')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, related_name='experts')
    speciality = models.CharField(max_length=255)
    experience_in_years = models.PositiveIntegerField(default=0)
    about = models.TextField()
    price_per_minute = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    schedule = models.TextField(blank=True)
    institution = models.CharField(max_length=255, blank=True)
    department = models.CharField(max_length=255, blank=True)
    passport_photo = models.ImageField(upload_to='passports/', blank=True)
    diploma_photo = models.ImageField(upload_to='diplomas/', blank=True)
    is_verified = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=['id'], name='id_index'),
        ]

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.speciality}'

    def get_absolute_url(self):
        return reverse('expert_detail', args=[self.id])
