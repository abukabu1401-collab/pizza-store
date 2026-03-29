from flask import Flask, render_template, request, redirect, url_for, flash
from repositrory.pizza_repository import PizzaRepository
from models.pizza import Pizza

app = Flask(__name__)
app.secret_key = 'pizza_secret_key'

# Создаем репозиторий
repo = PizzaRepository()

# Добавляем начальные пиццы
def add_initial_pizzas():
    pizzas = [
        Pizza("Маргарита", 450, ["томатный соус", "моцарелла", "базилик"], 30),
        Pizza("Пепперони", 550, ["томатный соус", "пепперони", "моцарелла"], 30),
        Pizza("Гавайская", 600, ["томатный соус", "курица", "ананас", "моцарелла"], 35),
        Pizza("Четыре сыра", 650, ["моцарелла", "пармезан", "горгонзола", "фонтина"], 35),
        Pizza("Мясная", 700, ["томатный соус", "бекон", "ветчина", "пепперони", "моцарелла"], 40),
        Pizza("Вегетарианская", 500, ["томатный соус", "грибы", "перец", "лук", "оливки"], 30),
    ]
    for pizza in pizzas:
        repo.add_pizza(pizza)


@app.route('/')
def index():
    """Главная страница"""
    pizzas = repo.get_all_pizzas()
    pizza_count = repo.get_pizza_count()
    
    # Вычисляем среднюю цену
    if pizza_count > 0:
        avg_price = sum(p.price for p in pizzas) / pizza_count
    else:
        avg_price = 0
    
    return render_template('index.html', 
                         pizzas=pizzas,
                         pizza_count=pizza_count,
                         avg_price=round(avg_price, 1))


@app.route('/add_pizza', methods=['GET', 'POST'])
def add_pizza():
    """Добавление пиццы"""
    if request.method == 'POST':
        name = request.form.get('name')
        price = int(request.form.get('price'))
        size = int(request.form.get('size'))
        ingredients_raw = request.form.get('ingredients', '')
        ingredients = [i.strip() for i in ingredients_raw.split(',') if i.strip()]
        
        repo.add_pizza_by_parameters(name, price, ingredients, size)
        flash(f"Пицца '{name}' добавлена!", 'success')
        return redirect(url_for('index'))
    
    return render_template('add_pizza.html')


@app.route('/edit_pizza/<name>', methods=['GET', 'POST'])
def edit_pizza(name):
    """Редактирование пиццы"""
    pizza = repo.update_pizza_by_name(name)
    
    if not pizza:
        flash(f"Пицца '{name}' не найдена", 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        new_name = request.form.get('name')
        new_price = int(request.form.get('price'))
        new_size = int(request.form.get('size'))
        ingredients_raw = request.form.get('ingredients', '')
        new_ingredients = [i.strip() for i in ingredients_raw.split(',') if i.strip()]
        
        # Обновляем через метод репозитория
        repo.update(name, new_name, new_price, new_ingredients, new_size)
        flash(f"Пицца обновлена!", 'success')
        return redirect(url_for('index'))
    
    return render_template('edit_pizza.html', pizza=pizza)


@app.route('/delete_pizza/<name>')
def delete_pizza(name):
    """Удаление пиццы"""
    if repo.delete_by_name(name):
        flash(f"Пицца '{name}' удалена", 'success')
    else:
        flash(f"Пицца '{name}' не найдена", 'error')
    return redirect(url_for('index'))


@app.route('/delete_all')
def delete_all():
    """Удаление всех пицц"""
    repo.delete_all_pizzas()
    flash("Все пиццы удалены", 'success')
    return redirect(url_for('index'))


@app.route('/sort_by_price')
def sort_by_price():
    """Сортировка по цене (дешевые сначала)"""


@app.route('/sort_by_price_desc')
def sort_by_price_desc():
    """Сортировка по цене (дорогие сначала)"""

@app.route('/sort_by_name')
def sort_by_name():
    """Сортировка по названию"""


@app.route('/sort_by_size')
def sort_by_size():
    """Сортировка по размеру"""


@app.route('/filter_by_price')
def filter_by_price():
    """Фильтр по цене"""
    min_price = request.args.get('min', type=int, default=0)
    max_price = request.args.get('max', type=int, default=10000)
    
    pizzas = repo.get_all_pizzas()
    filtered = [p for p in pizzas if min_price <= p.price <= max_price]
    
    return render_template('index.html', 
                         pizzas=filtered,
                         pizza_count=len(filtered),
                         sort_info=f"💰 Цена от {min_price} до {max_price}₽")


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Страница входа (только UI)"""
    if request.method == 'POST':
        # Здесь будет логика авторизации (следующий урок)
        flash("Авторизация будет добавлена позже!", 'info')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Страница регистрации (только UI)"""
    if request.method == 'POST':
        # Здесь будет логика регистрации (следующий урок)
        flash("Регистрация будет добавлена позже!", 'info')
    return render_template('register.html')


if __name__ == '__main__':
    add_initial_pizzas()
    app.run(debug=True)