#i have created this file - akhilesh kushwah


from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.POST.get('text','default')
    print(djtext)
    removepunc = request.POST.get('removepunc','off')
    extraspaceremove = request.POST.get('extraspaceremove','off')
    newlineremove = request.POST.get('newlineremove','off')
    charcounter = request.POST.get('charcounter','off')
    uppercase = request.POST.get('uppercase','off')
    
    if (removepunc=='on'):
        punctuations='''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''
        analyzed=''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'removed punctuations','analyzed_text':analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if(extraspaceremove=='on'):
        analyzed=''
        for index ,char in enumerate(djtext):
            if not(djtext[index]==' ' and djtext[index+1]==' '):
                analyzed=analyzed+char
        params = {'purpose':'removed extra spaces','analyzed_text':analyzed}
        djtext = analyzed
       # return render(request, 'analyze.html', params)  
    if(newlineremove=='on'):
        analyzed=''
        for char in djtext:
            if char !='\n' and char!='\r':
                analyzed = analyzed+char
        params={'purpose':'new line removed','analyzed_text':analyzed}
        djtext = analyzed
        #return render(request,'analyze.html',params)        

    if(charcounter=='on'):
        analyzed=djtext
        count=0
        for i in range (len(str(analyzed))):
            if not(analyzed[i]==' '):
                count=count+1
        params={'purpose':'character counted','analyzed_text':count}
        djtext = analyzed
        #return render(request,'analyze.html',params) 
    if(uppercase=='on'):
        analyzed=''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params={'purpose':'changed to uppercase','analyzed_text':analyzed}  
        djtext = analyzed
        #return render(request,'analyze.html',params)    
    if(removepunc !='on' and extraspaceremove !='on' and newlineremove !='on' and charcounter !='on' and uppercase !='on'):
        return HttpResponse("please select checkbox")
    
    return render(request,'analyze.html',params)                 