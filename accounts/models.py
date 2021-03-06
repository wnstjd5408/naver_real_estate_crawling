from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from locations.models import Apartment


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("must have user email address")

        user = self.model(
            email=self.normalize_email(email),
            # self.normalize_email? - >email을 정규화
            # -> @ 뒤에 값을 대소문자 구분 x로 만듦으로서 다중 가입 방지
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password=password, **extra_fields)
        user.is_admin = True

        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    email = models.EmailField(
        verbose_name="email",
        max_length=255,
        unique=True,
    )
    Gender_choices = {("M", "남자"), ("W", "여자")}
    name = models.CharField(max_length=15)
    date_of_birth = models.DateField(blank=True)
    gender = models.CharField(max_length=20, choices=Gender_choices)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "date_of_birth", "gender"]

    class Meta:
        db_table = "accounts"
        verbose_name = ("유저",)
        verbose_name_plural = "유저"

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Basket(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    uIDX = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE, verbose_name="회원", null=True)
    aIDX = models.ForeignKey(Apartment, on_delete=models.CASCADE, verbose_name="아파트", null=True)

    class Meta:
        verbose_name = "장바구니"
        verbose_name_plural = f"{verbose_name} 목록"

    def __str__(self):
        return str(self.uIDX) + "의 장바구니에서 " + str(self.aIDX)
