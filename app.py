from flask import Flask,render_template ,request,redirect

app = Flask(__name__)
@app.route('/')
def man():
    return render_template('a.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/calculate",methods=['POST'])
def calculate_exp():
    try:
        if request.method=='POST':
            exp=request.form['expression']
            if exp=="" or exp.isalpha():
                return render_template('a.html',exp="Invalid or No Input")
            print(exp)
            return render_template('a.html',exp=eval(exp))
    except:
        return redirect('/')

if __name__=="__main__":
    app.run(debug=True,port=8000)
