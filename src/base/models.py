from django.contrib.auth.models import User
from django.db import models


class TimeAuditModel(models.Model):
    ''' To track when the record was created and last modified'''
    created_at = models.DateTimeField('Created At',
                                      auto_now_add=True)
    updated_at = models.DateTimeField('Updated At',
                                      auto_now=True)

    class Meta:
        abstract = True


class UserAuditModel(models.Model):
    '''To track who created and last modified the record'''
    created_by = models.ForeignKey(User, related_name='created_%(class)s_set',
                                   null=True, blank=True, verbose_name='Created By',
                                   on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='updated_%(class)s_set',
                                   null=True, blank=True, verbose_name='Updated By',
                                   on_delete=models.CASCADE)

    class Meta:
        abstract = True


class AuditModel(TimeAuditModel, UserAuditModel):
    '''To track by who and when was the last record modified'''

    class Meta:
        abstract = True
