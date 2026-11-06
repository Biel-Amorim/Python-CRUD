from flask import Flask, render_template

app = Flask(__name__,template_folder='../templates/')

@app.get('/login')
def login_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)