from flask import Flask, render_template
import sqlite3
import random

DATABASE = "Events.db"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upcoming')
def upcoming():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    sql = "SELECT * FROM Event WHERE Status ='u' ORDER BY Dateorder ASC;"

    cursor.execute(sql)

    title = cursor.fetchall()

    db.close()
    print(title)
    return render_template('upcoming.html', title=title)

@app.route('/previous')
def previous():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    sql = "SELECT * FROM Event WHERE Status ='p' ORDER BY Dateorder DESC;"

    cursor.execute(sql)

    title = cursor.fetchall()

    db.close()
    print(title)
    return render_template('previous.html', title=title)

@app.route('/profile')
def profile():
   return render_template('profile.html')

@app.route('/outfits')
def outfits():
    top = random.randint(1, 22)
    print(top)
    bottom = random.randint(23, 43)
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    sql = "SELECT link FROM outfit WHERE id = ? ;"

    cursor.execute(sql,(top,))

    tops = cursor.fetchone()

    db.close()
    print(tops)
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    sql = "SELECT link FROM outfit WHERE id = ? ;"

    cursor.execute(sql,(bottom,))

    bottoms = cursor.fetchone()

    db.close()
    print(bottoms)
    return render_template('outfits.html', tops=tops, bottoms=bottoms)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
