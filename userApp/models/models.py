from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=100, default="")
    user_name = models.CharField(blank=False, null=False, max_length=200, unique=True)
    phone_no = models.CharField(db_index=True, blank=True, null=True, max_length=20, default="")
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'user'

    def __unicode__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(blank=True, null=True, default="", max_length=100, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'group'


class ActionType(models.Model):
    name = models.CharField(blank=True, null=True, default="", max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'action_types'


class Resource(models.Model):
    name = models.CharField(blank=True, null=True, default="", max_length=200)
    url = models.CharField(blank=True, null=True, default="", max_length=200, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'resources'


class UserGroup(models.Model):
    user = models.ForeignKey(User, blank=False, null=False)
    group = models.ForeignKey(Group, blank=False, null=False)
    active = models.BooleanField(blank=True, default=True)

    class Meta:
        db_table = 'user_groups'

    def __unicode__(self):
        return self.user.username + ' - ' + self.group.name


class ResourcePermission(models.Model):
    resource = models.ForeignKey(Resource, blank=False, null=False)
    action_type = models.ForeignKey(ActionType, blank=False, null=False)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'resource_permissions'


class ResourceGroupPermissions(models.Model):
    group = models.ForeignKey(Group, blank=False, null=False)
    resource_perm = models.ForeignKey(ResourcePermission, blank=False, null=False)
    active = models.BooleanField(blank=True, default=True)

    class Meta:
        db_table = 'resource_groups_permission'

    def __unicode__(self):
        return self.group.name + ' - ' + self.resource.name