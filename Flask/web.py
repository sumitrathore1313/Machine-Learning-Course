from flask import *  
app1 = Flask(__name__)  
  
@app1.route('/')  
def customer():  
   return render_template('customer.html')  
  
@app1.route('/success',methods = ['POST', 'GET'])  
def print_data():  
   if request.method == 'POST':  
      result = request.form  
      return render_template("result_data.html",result = result)  
   
if __name__ == '__main__':  
   app1.run(debug = True)  