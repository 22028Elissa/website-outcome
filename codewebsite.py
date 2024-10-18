from flask import Flask, render_template
import sqlite3

DATABASE = "Events.db"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upcoming')
def upcoming():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    sql = "SELECT * FROM Event;"

    cursor.execute(sql)

    title = cursor.fetchall()

    db.close()
    print(title)
    return render_template('upcoming.html', title=title)

@app.route('/previous')
def previous():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    sql = "SELECT * FROM Event;"

    cursor.execute(sql)

    title = cursor.fetchall()

    db.close()
    print(title)
    return render_template('previous.html', title=title)

@app.route('/profile')
def profile():
   return render_template('profile.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

