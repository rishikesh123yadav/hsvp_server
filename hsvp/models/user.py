from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin)
from django.core import validators
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.db.models import Manager

from phonenumber_field.modelfields import PhoneNumberField

HSVP_UNIQUE_CONTACT_NUMBER = getattr(settings, 'KEYLESS_UNIQUE_CONTACT_NUMBER', True)
HSVP_UNIQUE_EMAIL = getattr(settings, 'KEYLESS_UNIQUE_EMAIL', True)


class UserQuerySet(models.QuerySet):
    """
    Queryset for User model.

    """

    def get_by_natural_key(self, username):
        """
        Fetch the user by its username.
        Username should be case-insensitive.

        :param username:
        """
        return self.get(**{
            '{}__iexact'.format(self.model.USERNAME_FIELD): username
        })

    def active(self):
        """
        Filter all active users.
        """
        return self.filter(is_active=True)

    def inactive(self):
        """
        Filter all active users.
        """
        return self.exclude(is_active=False)

    @classmethod
    def normalize_email(cls, email):
        """
        Normalize the address by lowercasing the domain part of the email
        address.
        """
        email = email or ''
        try:
            email_name, domain_part = email.strip().rsplit('@', 1)
        except ValueError:
            pass
        else:
            email = '@'.join([email_name, domain_part.lower()])
        return email

    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, True, True,
                                 **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    A fully featured User model with admin-compliant permissions.
    Username, password and email are required. Other fields are optional.
    """
    username = models.CharField(
        _('username'), max_length=254, unique=True,
        help_text=_('required. 30 characters or fewer. letters, digits and '
                    '@/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(
                r'^[\w.@+-]+$', _('please enter a valid username. it may contain only letters, '
                                  'numbers and @/./+/-/_ characters.'), 'invalid')
        ],
        error_messages={
            'unique': _('username has already been taken.'),
        }
    )

    email = models.EmailField(
        _('email address'), unique=HSVP_UNIQUE_EMAIL,
        null=True, default=None,
        error_messages={
            'unique': _('email address is already registered.'),
        }
    )

    contact_number = PhoneNumberField(
        verbose_name=_('contact number'), unique=HSVP_UNIQUE_CONTACT_NUMBER,
        null=True, default=None,
        error_messages={
            'unique': _('contact number is associated with some other account. '
                        'please contact administrators if the number belongs to you.'),
        }
    )

    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)

    father_first_name = models.CharField(_('Father first name'), max_length=30, blank=True)
    father_last_name = models.CharField(_('Father last name'), max_length=30, blank=True)

    gst_no = models.CharField(_('GST No'), max_length=30, blank=True)

    otp = models.CharField(_('OTP sent to user'), max_length=10, blank=True)
    otp_sent_at = models.CharField(_('OTP sent at'), max_length=10, blank=True)

    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Deselect this instead of deleting accounts.'))

    date_invited = models.DateTimeField(_('date invited'), default=timezone.now)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = Manager.from_queryset(UserQuerySet)()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '{first} {last}'.format(first=self.first_name.capitalize(),
                                            last=self.last_name.capitalize())
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name
