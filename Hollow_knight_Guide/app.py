from flask import Flask, render_template

app = Flask(__name__)

# Расширенная база данных амулетов
charms_list = [
    {
        "id": "compass",
        "name": "Капризный компас",
        "slots": 1,
        "short_desc": "Показывает ваше местоположение на карте.",
        "full_desc": "Незаменимый инструмент для картографов и исследователей. Позволяет владельцу видеть свое точное местоположение на картах Корнифера.",
        "how_to_get": "Купите у Изельды в Гряземуте за 220 гео после встречи с Корнифером.",
        "img_url": "static/images/charms/compass.png",
        "map_url": "static/images/maps/compass_map.png"
    },
    {
        "id": "mark_of_pride",
        "name": "Метка гордости",
        "slots": 3,
        "short_desc": "Сильно увеличивает дистанцию удара гвоздем.",
        "full_desc": "Амулет, дарованный племенем богомолов тем, кого они признали достойными. Позволяет наносить удары с гораздо большего расстояния.",
        "how_to_get": "Находится в сундуке в Деревне Богомолов. Доступно только после победы над Лордами Богомолов.",
        "img_url": "static/images/charms/mark_of_pride.png",
        "map_url": "static/images/maps/pride_map.png"
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/charms')
def charms():
    return render_template('charms.html', charms=charms_list)

# Заглушки для остальных страниц (пока не меняем)
@app.route('/slots')
def slots(): return "В разработке"
@app.route('/vessels')
def vessels(): return "В разработке"
@app.route('/masks')
def masks(): return "В разработке"
@app.route('/abilities')
def abilities(): return "В разработке"
@app.route('/enemies')
def enemies(): return "В разработке"
@app.route('/endings')
def endings(): return "В разработке"

if __name__ == '__main__':
    app.run(debug=True)