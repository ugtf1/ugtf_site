from django.db import models

# Create your models here.
class Timestamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ScopingCall(Timestamped):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    preferred_contact_method = models.CharField(
        max_length=30,
        choices=[
            ("Phone", "Phone"),
            ("Email", "Email"),
            ("WhatsApp", "WhatsApp"),
            ("Zoom", "Zoom"),
        ],
    )

    def __str__(self):
        return f"{self.name} ({self.preferred_contact_method})"

class BriefMessage(Timestamped):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Brief from {self.name}"

class ContactMessage(Timestamped):
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    message = models.TextField()
    subscribe = models.BooleanField(default=False)

    def __str__(self):
        return f"Contact {self.email}"

class MailingListSubscriber(Timestamped):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email