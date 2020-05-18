# First flask program to connect sql server
#Created_by:Renuka Prasad
#Created_date:2020/05/18
#Updated_by:Renuka Prasad
#Updated_date:2020/05/18

from datetime import datetime    
from flask import render_template    
#from FlaskWebProject7 import app    
import pypyodbc      
from datetime import datetime    
    
from flask import render_template, redirect, request,Flask    
app = Flask(__name__)   
# creating connection Object which will contain SQL Server Connection    
connection = pypyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=Renuka;"
    "Database=Practice;"
    "Trusted_Connection=yes;"
)   
cursor = connection.cursor()    
cursor.execute("SELECT concat(employees.first_NAME,employees.Last_name) as employee_name,departments.DEPartment_NAME FROM departments \n"
"inner join employees on employees.department_id = departments.department_id where departments.department_name = 'Sales'")    
s = "<table style='border:1px solid red'>"    
for row in cursor:    
    s = s + "<tr>"    
    for x in row:    
        s = s + "<td style='border:1px solid blue'>" + str(x) + "</td>"    
    s = s + "</tr>"    
connection.close()    
   
@app.route('/')    
@app.route('/home')    
def home():    
    
    return "<html><body>" + s + "</body></html>" 

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 9000, app)