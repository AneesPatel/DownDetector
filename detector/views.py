from django.shortcuts import render
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
import requests
class NewTaskForm(forms.Form):
    input = forms.CharField(label="Add Website URL here")

def detect(website_url):

    response = requests.head(website_url)
    
    # check the status code
    if response.status_code == 200:
        return True
    else:
        return False
    
        

# Create your views here.
def index(request):
    
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            input = form.cleaned_data["input"]
            try:
                isItDown = detect(input)
                print(isItDown)
                return render(request, "detector/index.html", {
                "isItDown": isItDown
            })
            except:
                print("An error occured. Try Again.")
                return render(request, "detector/error.html")
            
            
    return render(request, "detector/index.html", {
        "form": NewTaskForm()
    })