from django.db import models

class Textbook(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    edition = models.CharField(max_length=50, blank=True, null=True)
    condition = models.CharField(
        max_length=50,
        choices=[
            ('New', 'New'),
            ('Written', 'Written'),
            ('Old', 'Old'),
        ]
    )
    course_code = models.CharField(max_length=10)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.course_code})"

