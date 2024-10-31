from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET' , 'POST'])
def index():
    user_input = ""
    if request.method == 'POST':
        user_input = request.form.get('xss_input', '')
    return render_template('index.html', user_input = user_input)
@app.route('/page2')
def hello_world2():
     return ('page')

@app.route('/login', methods=['GET' , 'POST'])
def login():
    user_input = ""
    if request.method == 'POST':
        user_input = request.form.get('username', '')
    return render_template('login.html', user_input = user_input)
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)


