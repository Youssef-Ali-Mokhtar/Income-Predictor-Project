from flask import request,Flask, render_template
import pickle

app=Flask(__name__,template_folder='C:/Users/Youssef/Desktop/final_project_dir')



"www.facebook.com/"
@app.route("/",methods=["GET"])
def first_function():
    return render_template("prediction.html")

"www.facebook.com/getlabel"
@app.route("/get_label",methods=["GET"])
def get_label():
    age=request.args.get("age")
    workclass=request.args.get("workclass")
    education=request.args.get("education")
    marital_status=request.args.get("marital-status")
    occupation=request.args.get("occupation")
    race=request.args.get("race")
    sex=request.args.get("sex")
    hours_per_week=request.args.get("hours-per-week")
    native_country=request.args.get("native-country")

    if workclass=="Federal-gov":
        workclass=0
    elif workclass=="Local-gov":
        workclass=1
    elif workclass=="Never-worked":
        workclass=2
    elif workclass=="Private":
        workclass=3
    elif workclass=="Self-emp-inc":
        workclass=4
    elif workclass=="Self-emp-not-inc":
        workclass=5
    elif workclass=="State-gov":
        workclass=6
    elif workclass=="Without-pay":
        workclass=7

    if education=="10th":
        education=0
    elif education=="11th":
        education=1
    elif education=="12th":
        education=2
    elif education=="1st-4th":
        education=3
    elif education=="5th-6th":
        education=4
    elif education=="7th-8th":
        education=5
    elif education=="9th":
        education=6
    elif education=="Assoc-acdm":
        education=7
    elif education=="Assoc-voc":
        education=8
    elif education=="Bachelors":
        education=9
    elif education=="Doctorate":
        education=10
    elif education=="HS-grad":
        education=11
    elif education=="Masters":
        education=12
    elif education=="Preschool":
        education=13
    elif education=="Prof-school":
        education=14
    elif education=="Some-college":
        education=15

    if marital_status=="Divorced":
        marital_status=0
    elif marital_status=="Married-AF-spouse":
        marital_status=1
    elif marital_status=="Married-civ-spouse":
        marital_status=2
    elif marital_status=="Married-spouse-absent":
        marital_status=3
    elif marital_status=="Never-married<":
        marital_status=4
    elif marital_status=="Separated":
        marital_status=5
    elif marital_status=="Widowed":
        marital_status=6

    if occupation=="Adm-clerical":
        occupation=0
    elif occupation=="Armed-Forces":
        occupation=1
    elif occupation=="Craft-repair":
        occupation=2
    elif occupation=="Exec-managerial":
        occupation=3
    elif occupation=="Farming-fishing":
        occupation=4
    elif occupation=="Handlers-cleaners":
        occupation=5
    elif occupation=="Machine-op-inspct":
        occupation=6
    elif occupation=="Other-service":
        occupation=7
    elif occupation=="Priv-house-serv":
        occupation=8
    elif occupation=="Prof-specialty":
        occupation=9
    elif occupation=="Protective-serv":
        occupation=10
    elif occupation=="Sales":
        occupation=11
    elif occupation=="Tech-support":
        occupation=12
    elif occupation=="Transport-moving":
        occupation=13

    if race=="Amer-Indian-Eskimo":
        race=0
    elif race=="Asian-Pac-Islander":
        race=1
    elif race=="Black":
        race=2
    elif race=="Other":
        race=3
    elif race=="White":
        race=4

    if sex=="Female":
        sex=0
    elif sex=="Male":
        sex=1

    if native_country=="Cambodia":
        native_country=0
    elif native_country=="Canada":
        native_country=1
    elif native_country=="China":
        native_country=2
    elif native_country=="Columbia":
        native_country=3
    elif native_country=="Cuba":
        native_country=4
    elif native_country=="Dominican-Republic":
        native_country=5
    elif native_country=="Ecuador":
        native_country=6
    elif native_country=="El-Salvador":
        native_country=7
    elif native_country=="England":
        native_country=8
    elif native_country=="Greece":
        native_country=9
    elif native_country=="Germany":
        native_country=10
    elif native_country=="France":
        native_country=11
    elif native_country=="Guatemala":
        native_country=12
    elif native_country=="Haiti":
        native_country=13
    elif native_country=="Holand-Netherlands":
        native_country=14
    elif native_country=="Honduras":
        native_country=15
    elif native_country=="Hong":
        native_country=16
    elif native_country=="Hungary":
        native_country=17
    elif native_country=="India":
        native_country=18
    elif native_country=="Iran":
        native_country=19
    elif native_country=="Ireland":
        native_country=20
    elif native_country=="Italy":
        native_country=21
    elif native_country=="Jamaica":
        native_country=22
    elif native_country=="Japan":
        native_country=23
    elif native_country=="Thailand":
        native_country=24
    elif native_country=="Mexico":
        native_country=25
    elif native_country=="Nicaragua":
        native_country=26
    elif native_country=="Outlying-US(Guam-USVI-etc)":
        native_country=27
    elif native_country=="Peru":
        native_country=28
    elif native_country=="Philippines":
        native_country=29
    elif native_country=="Poland":
        native_country=30
    elif native_country=="Portugal":
        native_country=31
    elif native_country=="Puerto-Rico":
        native_country=32
    elif native_country=="Scotland":
        native_country=33
    elif native_country=="South":
        native_country=34
    elif native_country=="Taiwan":
        native_country=35
    elif native_country=="Laos":
        native_country=36
    elif native_country=="Trinadad&Tobago":
        native_country=37
    elif native_country=="United-States":
        native_country=38
    elif native_country=="Vietnam":
        native_country=39
    elif native_country=="Yugoslavia":
        native_country=40


    model=pickle.load(open("C:/Users/Youssef/Desktop/final_project_dir/saved_final_model.pk", 'rb'))
    result=model.predict([[age,workclass,education,marital_status
    ,occupation,race,sex,hours_per_week,native_country]])
    if result==1:
        result=">50K"
    else:
        result="<=50K"
    return "<h1>"+result+"</h1>"



if __name__ == '__main__':
    app.run(host="127.0.0.1",port=9090)