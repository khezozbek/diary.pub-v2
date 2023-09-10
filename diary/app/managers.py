def create_user(self, username, password=None, type='Teacher', **extra_fields):
    extra_fields.setdefault('type', type)
    return self._create_user(username, password, **extra_fields)
