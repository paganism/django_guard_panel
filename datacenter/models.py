from django.db import models
from datetime import datetime, timezone


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )

    def get_duration(self):
        now = datetime.now(timezone.utc)
        if self.leaved_at == None:
            return now - self.entered_at
        else:
            return self.leaved_at - self.entered_at

    def format_duration(self, duration):
        seconds = duration.seconds
        hours = seconds // 3600
        remaining_seconds = seconds - (hours * 3600)
        minutes = remaining_seconds // 60
        return '{} ч {} мин'.format(hours, minutes)

    def is_visit_long(self, duration):
        if duration.seconds <= 3600:
            return False
        return True
