from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Crea el superusuario y varios usuarios con distintos roles de ejemplo'

    def handle(self, *args, **options):
        # Superusuario
        admin, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@example.com',
                'is_superuser': True,
                'is_staff': True
            }
        )
        if created:
            admin.set_password('admin123')
            admin.save()
            self.stdout.write(self.style.SUCCESS('🧠 Superusuario creado: admin / admin123'))
        else:
            self.stdout.write(self.style.WARNING('🧠 Superusuario ya existe: admin'))

        # Staff (no superuser)
        staff, created = User.objects.get_or_create(
            username='staff',
            defaults={'email': 'staff@example.com'}
        )
        if created:
            staff.set_password('staff123')
            staff.is_staff = True
            staff.save()
            self.stdout.write(self.style.SUCCESS('👔 Usuario staff creado: staff / staff123'))

        # Usuario activo común
        user, created = User.objects.get_or_create(
            username='user',
            defaults={'email': 'user@example.com'}
        )
        if created:
            user.set_password('user123')
            user.save()
            self.stdout.write(self.style.SUCCESS('🧍 Usuario común creado: user / user123'))

        # Usuario no activo
        disabled, created = User.objects.get_or_create(
            username='disabled',
            defaults={'email': 'disabled@example.com'}
        )
        if created:
            disabled.set_password('disabled123')
            disabled.is_active = False
            disabled.save()
            self.stdout.write(self.style.SUCCESS('🚫 Usuario desactivado creado: disabled / disabled123'))

        self.stdout.write(self.style.SUCCESS('✅ Usuarios iniciales generados.'))
