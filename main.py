from datetime import datetime

class Greeter:
    def greet(self, name):
        # Trcorte en la entrada
        name = name[:3]

        # mayúscula la primera letra del nombre
        name = name.capitalize()

        # Obtiene la hora actual
        current_time = datetime.now().time()

        # Determina el saludo según la hora del día
        if datetime.strptime("06:00", "%H:%M").time() <= current_time < datetime.strptime("12:00", "%H:%M").time():
            return f"Good morning {name}"
        elif datetime.strptime("18:00", "%H:%M").time() <= current_time < datetime.strptime("22:00", "%H:%M").time():
            return f"Good evening {name}"
        else:
            return f"Good night {name}"