from django.shortcuts import render
from django.http import HttpResponse
import joblib
import pickle


def home(request):
    return render(request,"Home.html")
def result(request):
    pickle_in=open('classifier.pkl','rb')
    classifier=pickle.load(pickle_in)



    lis=[]
    lis.append(request.POST["t1"])
    lis.append(request.POST["t2"])
    lis.append(request.POST["t3"])
    lis.append(request.POST["t4"])
    ans=classifier.predict([lis])
    return render(request,"Home.html",{"ans":ans})


#cls=joblib.load('finalised_model.sav')