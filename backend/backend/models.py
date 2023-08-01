# # models.py
# from django.db import models
# from django.contrib.auth.models import User


# class Appointment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     service_name = models.CharField(max_length=100)
#     date = models.DateField()
#     time = models.TimeField()
#     STATUS_CHOICES = (
#         ('Pending', 'Pending'),
#         ('Fixed', 'Fixed'),
#     )
#     status = models.CharField(
#         max_length=10, choices=STATUS_CHOICES, default='Pending')

#     def __str__(self):
#         return f"{self.service_name} on {self.date} at {self.time}"
