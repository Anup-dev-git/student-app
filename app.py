from flask import Flask, render_template, request
import sqlite3 
app = Flask(__name__)
port=5000 

con = sqlite3.connect("student.db")  
con.execute("create table if not exists student (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, enroll TEXT UNIQUE NOT NULL, branch TEXT NOT NULL)")   
 
@app.route("/")  
def index():  
    return render_template("index.html"); 
 
@app.route("/add")  
def add():  
    return render_template("add.html")  
  
@app.route("/savedetails",methods = ["POST","GET"])  
def saveDetails():  
    msg = "msg" 
    if request.method == "POST":  
        try:  
            name = request.form["name"]  
            enroll = request.form["enroll"]  
            branch = request.form["branch"]  
            with sqlite3.connect("student.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into student (name, enroll, branch) values (?,?,?)",(name,enroll,branch))  
                con.commit()  
                msg = "Student details added" 
        except:  
            con.rollback()  
            msg = "Students details can't be added" 
        finally:  
            return render_template("success.html",msg = msg)  
            con.close()   
 
@app.route("/view")  
def view():  
    con = sqlite3.connect("student.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from student")  
    rows = cur.fetchall()  
    return render_template("view.html",rows = rows)   
 
@app.route("/delete")  
def delete():  
    return render_template("delete.html")  
 
@app.route("/deleterecord",methods = ["POST"])  
def deleterecord():  
    id = request.form["id"]  
    with sqlite3.connect("student.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("delete from student where id = ?",id)  
            msg = "student record successfully removed" 
        except:  
            msg = "record not deleted" 
        finally:  
            return render_template("delete_record.html",msg = msg)
    
if __name__ == '__main__':
   app.run(host="0.0.0.0",port=port)