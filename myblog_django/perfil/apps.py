from django.apps import AppConfig


class PerfilConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'perfil'
    verbose_name = 'Perfiles' #Cambia el nombre a la app en la interfaz del admin, sustituyo el de arriba
