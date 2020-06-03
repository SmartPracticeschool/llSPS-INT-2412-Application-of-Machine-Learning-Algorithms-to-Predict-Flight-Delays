from flask import Flask , render_template,request
import pickle
app=Flask(__name__ )
model=pickle.load(open('flightdelay.pkl','rb'))

@app.route('/')
def hello_world():
    return render_template('flight.html')
@app.route('/login',methods=["POST"])
def login():
    d=request.form["d"]
    if(d=="ATL"):
        d1,d2,d3,d4,d5=1,0,0,0,0
    if(d=="DTW"):
        d1,d2,d3,d4,d5=0,1,0,0,0
    if(d=="JFK"):
        d1,d2,d3,d4,d5=0,0,1,0,0
    if(d=="MSP"):
        d1,d2,d3,d4,d5=0,0,0,1,0
    if(d=="SEA"):
        d1,d2,d3,d4,d5=0,0,0,0,1
    o=request.form["o"]   
    if(o=="ATL"):
        o1,o2,o3,o4,o5=1,0,0,0,0
    if(o=="DTW"):
        o1,o2,o3,o4,o5=0,1,0,0,0
    if(o=="JFK"):
        o1,o2,o3,o4,o5=0,0,1,0,0
    if(o=="MSP"):
        o1,o2,o3,o4,o5=0,0,0,1,0
    if(o=="SEA"):
        o1,o2,o3,o4,o5=0,0,0,0,1
    yr=request.form["yr"]
    mo=request.form["mo"]
    dm=request.form["dm"]
    dw=request.form["dw"]
    fn=request.form["fn"]
    sd=request.form["sd"]
    ad=request.form["ad"]
    sa=request.form["sa"]
    aa=request.form["aa"]
    di=request.form["di"]
    de=request.form["de"]
    delay=[[d1,d2,d3,d4,d5,o1,o2,o3,o4,o5,int(yr),int(mo),int(dm),int(dw),int(fn),int(sd),int(ad),int(sa),int(aa),int(di),int(de)]]
    
    p=model.predict(delay)
 
    return render_template('flight.html',label="the flight is ="+str(p))

if __name__=='__main__':
    app.run(debug=True,port=9000)

