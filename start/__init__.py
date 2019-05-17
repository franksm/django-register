

from user.models import Doctor
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

content_type = ContentType.objects.get_for_model(Doctor)
permission = Permission.objects.create(codename='can_view', name='Can view Doctor', content_type=content_type)
permission = Permission.objects.create(codename='can_add', name='Can add Doctor', content_type=content_type)
permission = Permission.objects.create(codename='can_see', name='Can see Doctor', content_type=content_type)
permission = Permission.objects.create(codename='can_edit', name='Can edit Doctor', content_type=content_type)
permission = Permission.objects.create(codename='can_delete', name='Can delete Doctor', content_type=content_type)
