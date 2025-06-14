from flask import Flask, url_for, redirect, request, render_template
import pickle,os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home_page.html")

@app.route('/read_form', methods=['POST'])
def read_form():
    if request.method == 'POST':
        Sentence = request.form.get('Sentence')
        # password = request.form.get('userPassword')
        # contact = request.form.get('userContact')
        # gender = request.form.get('gender')
        # newsletter = request.form.get('newsletter')
        
        # # Pass the form data to the template
        # form_data = {
        #     'email': email,
        #     'password': password,
        #     'contact': contact,
        #     'gender': gender,
        #     'newsletter': newsletter
        # }
        d=dict()
        d={0:"Negative",1:"Neutral",2:"Positive"}
        lrf=pickle.load(open(os.path.join("..","pickled","lrp_model.pkl"),"rb"))
        
        return d[int(lrf.predict([Sentence])[0])]
@app.route('/user/')
def users():
    return 'users'

@app.route('/user/<username>')
def show_username(usernames):
    return f'Hello, {usernames}!'

@app.route('/redirect-to-user')
def redirect_to_user():
    return redirect(url_for('show_username', username='nisha'))

if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)
