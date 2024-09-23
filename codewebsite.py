from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/upcoming')
def upcoming():
    return render_template('upcoming.html')
@app.route('/previous')
def previous():
    return render_template('previous.html')
@app.route('/profile')
def profile():
   return render_template('profile.html')
#@app.route('/interact')
#def interact():
#return render_template('interact.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

