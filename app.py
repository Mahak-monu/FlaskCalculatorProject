from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/math', methods=["POST"])
def math_ops():
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        operation = request.form['operation']
        if operation== 'add':
            ans = num1+num2
            result = f" The Addition of {num1} and {num2} is : {ans}" 
        elif operation == 'subtract':
            ans = num1-num2
            result = "The Subtraction of "+str(num1)+" and "+str(num2)+" is : "+str(ans)
        elif operation == 'multiply' :
            ans = num1*num2
            result = f"The Multiplication of {num1} ans {num2} is : {ans}"
        elif operation == 'divide' :
            ans = num1/num2
            result = f"The Divison of {num1} and {num2} is : {ans}"  
        elif operation == 'modulo':
            ans = num1%num2
            result = f"The Modulo of {num1} and {num2} is : {ans}"    
    return render_template('results.html', my_result = result)

@app.route('/postman_action', methods=["POST"])
def math_ops_post():
    if request.method == "POST":
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        operation  = request.json['operation']
        if operation== 'add':
            ans = num1+num2
            result = f" The Addition of {num1} and {num2} is : {ans}" 
        elif operation == 'subtract':
            ans = num1-num2
            result = "The Subtraction of "+str(num1)+" and "+str(num2)+" is : "+str(ans)
        elif operation == 'multiply' :
            ans = num1*num2
            result = f"The Multiplication of {num1} ans {num2} is : {ans}"
        elif operation == 'divide' :
            ans = num1/num2
            result = f"The Divison of {num1} and {num2} is : {ans}"  
        elif operation == 'modulo':
            ans = num1%num2
            result = f"The Modulo of {num1} and {num2} is : {ans}"
        return jsonify(result)


if __name__ == '__main__':
    app.run(host="0.0.0.0")