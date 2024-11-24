from django.shortcuts import render
import mysql.connector as sql
from django.http import HttpResponse
# Create your views here.
def login_app(request):
    global em,pas
    if request.method=='POST':
        m=sql.connect(host="localhost", user="root",password="Geometry+3",database="matrimony")
        cursor=m.cursor()
        d=request.post
        for key,value in d.items():
            if key=="email":
               em=value
            if key=="password":
               pas=value
        c="SELECT * FROM profile WHERE Email=%s AND Password=%s"
        values=(em,pas) 
        cursor.execute(c,values)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            user_details=t[0]
            context ={
                'user_name' :user_details[0],
                'gender' :user_details[1],
                'age' :user_details[2],
                'caste' : user_details[3],
                'Height':user_details[4],
                'weight':user_details[5],
                'mother_tangue' : user_details[6],
                'DOB':user_details[7],
                'M-status': user_details[8],
                'F-status':user_details[9],
                'F-type' :user_details[10],
                'F-values' :user_details[11],
                'Disability' :user_details[12],
                'education' :user_details[13],
                'occupaion' :user_details[14],
                'Income' :user_details[15],
                'Employed_in':user_details[16]
            }
            return render(request,'Home.html',context)
        # m.commit() 
    
    return render(request,'login.html') 
            


    