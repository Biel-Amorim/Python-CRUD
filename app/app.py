from flask import Flask, render_template, request

app = Flask(__name__,template_folder='templates/')

@app.get('/')
def login_page():
    return render_template('login.html')

@app.post('/verify-login')
def receive_post_login():
    user_post = request.form.get('user')
    pwd_post = request.form.get('password')
    print(user_post, pwd_post)
    return [user_post, pwd_post]


if __name__ == '__main__':
    app.run(debug=True)