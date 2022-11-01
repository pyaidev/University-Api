from django.db import models


class About(models.Model):
    title = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='About')

    def __str__(self):
        return self.title


class Service(models.Model):
    service_icon = models.ImageField(upload_to='Service_icon')
    service_title = models.CharField(max_length=212)
    service_content = models.TextField()

    def __str__(self):
        return self.service_title


class Reason(models.Model):
    reason_title = models.CharField(max_length=212)
    reason_content = models.TextField()
    reason_image = models.ImageField(upload_to='Reason')

    def __str__(self):
        return self.reason_title


class FAQ(models.Model):
    question = models.CharField(max_length=212)
    answer = models.TextField()

    def __str__(self):
        return self.question
