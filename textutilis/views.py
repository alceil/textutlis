from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analyse(request):
    djtext= request.POST.get('text','default')
    removepunc=request.POST.get('removepunc', 'default')
    fullcaps = request.POST.get('fullcaps', 'default')
    newlineremover = request.POST.get('newlineremover', 'default')
    extraspaceremover = request.POST.get('extraspaceremover', 'default')
    print(djtext)
    print(removepunc)
    if removepunc == "on":
    #analysed=djtext
        punctuations="!#$%&'()*+, -./:;<=>?@[\]^_`{|}~"
        analysed=""
        for char in djtext:
            if char not in punctuations:
                analysed=analysed+char
        params={'purpose':'Removed Punctuations','analysed_text':analysed}
        djtext = analysed
        #return render(request,'analyse.html',params)
    if(fullcaps=="on"):
        analysed = ""
        for char in djtext:
            analysed=analysed + char.upper()

        params={'purpose':'Changed to uppercase','analysed_text':analysed}
        djtext = analysed
        #return render(request,'analyse.html',params)

    if (newlineremover == "on"):
        analysed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analysed = analysed + char

        params = {'purpose': 'Removed NewLines', 'analysed_text': analysed}
        djtext = analysed
        #return render(request, 'analyse.html', params)
    if (extraspaceremover == "on"):
        analysed = ""
        for index,char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1]:
                analysed = analysed + char
        params = {'purpose': 'Removed NewLines', 'analysed_text': analysed}
        djtext = analysed
        #return render(request, 'analyse.html', params)
    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps!="on"):
        return HttpResponse("please select the appropriate option")
    return render(request, 'analyse.html', params)
