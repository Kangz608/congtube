from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


ACTIVE = 1
DELETE = 2
REST = 3
BAN = 4

USER_STATUS = (
    (ACTIVE, 'ACTIVE'),
    (DELETE, 'DELETE'),  # 회원탈퇴
    (REST, 'REST'),  # 휴면계정
    (BAN, 'BAN'),  # 밴
)

CUSTOMER = 1
STAR = 2

ROLES = (
    (CUSTOMER, 'CUSTOMER'),
    (STAR, 'STAR'),
)


class UserManager(BaseUserManager):
    def create_user(self, email, agree_terms, agree_marketing, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            agree_terms=agree_terms,
            agree_marketing=agree_marketing,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, agree_terms, agree_marketing, password):
        user = self.create_user(
            email,
            password=password,
            agree_terms=agree_terms,
            agree_marketing=agree_marketing,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    agree_terms = models.BooleanField(default=False)
    agree_marketing = models.BooleanField(default=False)
    status = models.PositiveIntegerField(choices=USER_STATUS, default=1)
    roles = models.PositiveIntegerField(choices=ROLES, default=1)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['agree_terms', 'agree_marketing']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
