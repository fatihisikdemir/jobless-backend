from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Crea el superusuario y varios usuarios con distintos roles de ejemplo'

    def handle(self, *args, **options):
        # Superusuario
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123'
            )
            self.stdout.write(self.style.SUCCESS('🧠 Superusuario creado: admin / admin123'))
        else:
            self.stdout.write(self.style.WARNING('🧠 Superusuario ya existe: admin'))

        # Staff (no superuser)
        if not User.objects.filter(username='staff').exists():
            staff = User.objects.create_user(
                username='staff',
                email='staff@example.com',
                password='staff123'
            )
            staff.is_staff = True
            staff.save()
            self.stdout.write(self.style.SUCCESS('👔 Usuario staff creado: staff / staff123'))

        # Usuario activo común
        if not User.objects.filter(username='user').exists():
            User.objects.create_user(
                username='user',
                email='user@example.com',
                password='user123'
            )
            self.stdout.write(self.style.SUCCESS('🧍 Usuario común creado: user / user123'))

        # Usuario no activo
        if not User.objects.filter(username='disabled').exists():
            disabled = User.objects.create_user(
                username='disabled',
                email='disabled@example.com',
                password='disabled123'
            )
            disabled.is_active = False
            disabled.save()
            self.stdout.write(self.style.SUCCESS('🚫 Usuario desactivado creado: disabled / disabled123'))

        self.stdout.write(self.style.SUCCESS('✅ Usuarios iniciales generados.'))
