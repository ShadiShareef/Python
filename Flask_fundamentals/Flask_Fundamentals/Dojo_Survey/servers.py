from flask import Flask, render_template,request
app = Flask(__name__)
# our index route will handle rendering our form

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['YourName']
    Location_from_form = request.form['Dojo Location']
    Language_from_form = request.form['Favorite Language']
    text_from_form = request.form['text']
    return render_template("result.html", name_on_template=name_from_form ,Location_on_template=Location_from_form, Language_on_template=Language_from_form,text_on_template=text_from_form )

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)