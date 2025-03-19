from django.db import models
from django.contrib.auth.models import User

class Courses(models.Model):
    student = models.ManyToManyField(User, related_name='courses',verbose_name="Student Name", blank=False)
    course = models.CharField(blank=False, verbose_name="Course", max_length=150)
    is_active = models.BooleanField(default=True, verbose_name="Status")
    created_at = models.DateTimeField(auto_now_add = True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now = True,verbose_name="Updated Date")

    def __str__(self):
        return self.course
    class Meta:
        verbose_name = "Courses"
        verbose_name_plural = "Courses"


