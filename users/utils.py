from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def _create_user_(
        self,
        email,
        password,
        first_name,
        last_name,
        is_seller,
        is_staff,
        is_superuser,
        **extra_fields
    ):

        if not email:
            raise ValueError("Need an email.")

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            is_seller=is_seller,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=True,
            **extra_fields
        )

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_user(
        self, email, password, first_name, last_name, is_seller, **extra_fields
    ):
        return self._create_user_(
            email,
            password,
            first_name,
            last_name,
            is_seller,
            True,
            False,
            **extra_fields
        )

    def create_superuser(
        self, email, password, first_name, last_name, **extra_fields
    ):
        return self._create_user_(
            email,
            password,
            first_name,
            last_name,
            False,
            True,
            True,
            **extra_fields
        )
