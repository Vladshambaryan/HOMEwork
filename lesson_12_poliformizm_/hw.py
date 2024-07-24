
class Flower:
    def __init__(self, name, color, stem_length, cost, freshness_days):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.cost = cost
        self.freshness_days = freshness_days

    def __repr__(self):
        return f"{self.name} ({self.color})"

# Классы для конкретных видов цветов
class Rose(Flower):
    def __init__(self, color, stem_length, cost, freshness_days):
        super().__init__('Роза', color, stem_length, cost, freshness_days)

class Tulip(Flower):
    def __init__(self, color, stem_length, cost, freshness_days):
        super().__init__('Тюльпан', color, stem_length, cost, freshness_days)

class Lily(Flower):
    def __init__(self, color, stem_length, cost, freshness_days):
        super().__init__('Лилии', color, stem_length, cost, freshness_days)

# Класс для букета
class Bouquet:
    def __init__(self, flowers=None):
        self.flowers = flowers if flowers is not None else []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def total_cost(self):
        return sum(flower.cost for flower in self.flowers)

    def average_freshness(self):
        if not self.flowers:
            return 0
        return sum(flower.freshness_days for flower in self.flowers) / len(self.flowers)

    def sort_by(self, attribute):
        valid_attributes = ['freshness_days', 'color', 'stem_length', 'cost']
        if attribute in valid_attributes:
            self.flowers.sort(key=lambda flower: getattr(flower, attribute))
        else:
            raise ValueError(f"Invalid attribute for sorting: {attribute}")

    def search_by(self, **criteria):
        results = self.flowers
        for attribute, value in criteria.items():
            results = [flower for flower in results if getattr(flower, attribute) == value]
        return results

    def __repr__(self):
        return f"Букет с {len(self.flowers)} цветы: {self.flowers}"

# Создание экземпляров цветов
rose1 = Rose(color='red', stem_length=50, cost=100, freshness_days=7)
tulip1 = Tulip(color='yellow', stem_length=30, cost=50, freshness_days=5)
lily1 = Lily(color='white', stem_length=40, cost=80, freshness_days=6)

# Создание букета
bouquet = Bouquet()
bouquet.add_flower(rose1)
bouquet.add_flower(tulip1)
bouquet.add_flower(lily1)

# Вывод информации о букете
print(bouquet)
print(f"Общая стоимость: {bouquet.total_cost()} руб")
print(f"Средняя свежесть: {bouquet.average_freshness()} дней")

# Сортировка цветов в букете по стоимости
bouquet.sort_by('cost')
print("После сортировки по стоимости:", bouquet)

# Поиск цветов в букете по цвету
search_results = bouquet.search_by(color='red')
print("Цветы красного цвета:", search_results)
