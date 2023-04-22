from django.db import models


class UserContact(models.Model):
    """ A model for user contact form """

    name_surname = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    details = models.CharField(max_length=55, null=False, blank=False)
    enquiry = models.TextField(max_length=220, null=False, blank=False)


class NewsLetter(models.Model):
    """ A model for subscription to newsletter """

    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.email
