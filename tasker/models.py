from django.db import models

# Create your models here.

class ClientTask(models.Model):
	clientname = models.CharField(max_length=255, unique=True)
	clientaction = models.CharField(max_length=255, unique=True)
	tasktime = models.DateTimeField(null=True)
	action_completed = models.BooleanField(default=False)

	def complete_action(self):
		from django.utils import timezone
		if self.tasktime > timezone.datetime():
			self.action_completed=True
			return True
		return False