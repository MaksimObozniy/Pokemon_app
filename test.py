from pokemon_entities.models import Pokemon

# Найти покемона
ivysaur = Pokemon.objects.get(title="Ивизавр")

# Проверить предыдущую эволюцию
print(ivysaur.previous_evolution)  # Ожидается: Бульбазавр

# Проверить следующие эволюции
print(ivysaur.next_evolutions.all())  # Ожидается: Венузавр