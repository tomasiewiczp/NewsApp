from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/select_category')
def select_category():
    return render_template('select_category.html')

@app.route('/handle_selection', methods=['GET', 'POST'])
def handle_selection():
    if request.method == 'POST':
        category = request.form['category']
        # Logika obsługi wybranej kategorii
        return f"You selected {category}"
    else:
        # Logika dla metody GET (np. wyświetlenie formularza)
        return render_template('select_category.html')


if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
