from flask import *  
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/hello') #decorator drfines the   
def hello():  
    return "hello, this is our first flask website";  

 
@app.route('/') #decorator drfines the   
def home():  
    return render_template('mesg.html')  

@app.route('/getData',methods = ['POST', 'GET', 'PATCH'])
def getData():
    if request.method == 'POST':  
        print("POST", request)
        return jsonify(request.form)
    elif request.method == 'GET':
        print("GET", request)
        return jsonify(request.args)
    else:
        return jsonify({'mesg': ''})

@app.route('/mesg/<id>')
def mesg(id):
    return jsonify({'mesg': id})


if __name__ == '__main__':  
    app.run(debug = True)  