import pulp

# Створимо проблему максимізації
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні рішення: кількість виробленого лимонаду і фруктового соку
x = pulp.LpVariable('Limonade', lowBound=0, cat='Integer')
y = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

# Цільова функція: максимізація кількості вироблених продуктів
model += x + y, "Total_Production"

# Обмеження на ресурси
model += 2 * x + y <= 100, "Water_Limit"         # Вода
model += x <= 50, "Sugar_Limit"                  # Цукор
model += x <= 30, "Lemon_Juice_Limit"            # Лимонний сік
model += 2 * y <= 40, "Fruit_Puree_Limit"        # Фруктове пюре

# Розв'язуємо задачу
model.solve()

# Результати
limonade_qty = pulp.value(x)
fruit_juice_qty = pulp.value(y)
total_production = pulp.value(model.objective)

print(f"Кількість виробленого Лимонаду: {limonade_qty}")
print(f"Кількість виробленого Фруктового соку: {fruit_juice_qty}")
print(f"Загальна кількість вироблених продуктів: {total_production}")
