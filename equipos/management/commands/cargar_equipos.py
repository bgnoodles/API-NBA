from django.core.management.base import BaseCommand
from equipos.models import Equipo
import requests

class Command(BaseCommand):
    help = "Carga datos de equipos NBA desde la API externa"

    def handle(self, *args, **kwargs):
        api_key = "225cbe7f-49ca-4a45-848f-9bf35c520826"
        url = "https://api.balldontlie.io/v1/teams"
        headers = {'Authorization': f'Token {api_key}'}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

            if response.status_code == 200:
                self.process_teams(response.json())

                # Check for pagination
                while 'next' in response.json().get('meta', {}):
                    next_url = response.json()['meta']['next']
                    response = requests.get(next_url, headers=headers)
                    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
                    if response.status_code == 200:
                        self.process_teams(response.json())
                    else:
                        self.stdout.write(self.style.ERROR(f"Error al consumir la API: {response.status_code}"))
                        break
            else:
                self.stdout.write(self.style.ERROR(f"Error al consumir la API: {response.status_code}"))

        except requests.exceptions.HTTPError as e:
            self.stdout.write(self.style.ERROR(f"HTTP error occurred: {e}"))

        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR(f"Request error occurred: {e}"))

    def process_teams(self, data):
        equipos_data = data.get('data', [])
        for equipo_data in equipos_data:
            equipo, created = Equipo.objects.get_or_create(
                nombre=equipo_data['full_name'],
                defaults={
                    'ciudad': equipo_data['city'],
                    'conferencia': equipo_data['conference'],
                    'division': equipo_data['division'],
                    'nombre_completo': equipo_data['full_name'],
                    'abreviacion': equipo_data['abbreviation']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Equipo {equipo.nombre} creado"))
            else:
                self.stdout.write(self.style.WARNING(f"Equipo {equipo.nombre} ya existe"))
