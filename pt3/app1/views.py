from django.shortcuts import render, HttpResponse, redirect

def index(request):
        return render(request, "index.html")

#GET Method
def Istanbul(request):
    return render(request, "Istanbul.html")

def Trabzon(request):
    return render(request, "Trabzon.html")


def register_again(request):
    return render(request, "register_again.html")


def process (request):
        form_check=request.POST["Turkey_Tours"]
        if form_check=='Trabzon':
            first_name= request.POST.get("first_name")
            last_name= request.POST.get("last_name")
            check_human= request.POST.get("check_human")
            request.session["first_name"] = first_name
            request.session["last_name"] = last_name
            if check_human !='4cVbQx9' or check_human==" " :
                return redirect("/register_again")
            return redirect("/Trabzon")
        if form_check=='Istanbul':
            first_name= request.POST.get("first_name")
            last_name= request.POST.get("last_name")
            check_human= request.POST.get("check_human")
            request.session["first_name"] = first_name
            request.session["last_name"] = last_name
            if check_human !='24w2ZAq' or check_human==" " :
                return redirect("/register_again")
            return redirect("/Istanbul")
        return redirect("/")


