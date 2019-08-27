from flask import *  
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/hello') #decorator drfines the   
def hello():  
    return "hello, this is our first flask website";  

 
@app.route('/') #decorator drfines the   
def home():  
    return render_template('mesg.html')  



if __name__ =='__main__':  
    app.run(debug = True)  