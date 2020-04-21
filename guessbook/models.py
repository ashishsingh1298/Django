from django.db import models

from django.utils import timezone


class Comment(models.Model):
	name = models.TextField()
	comment = models.TextField()
	date_added = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return '<Name: {}, ID: {}>'.format(self.name, self.id)
