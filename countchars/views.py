from django.http import HttpResponse
from django.shortcuts import render

import operator

def vwelnote(request):
    return HttpResponse("\n Welcome , Django first Project")

def vwelfile(request):
    return render(request,"Welcome.html")

def vcountfile(request):
    ft=request.GET['fulltext']

    wrdlist=ft.split()
    wrddict={}
    for word in wrdlist:
        if word in wrddict:
            wrddict[word]+=1
        else:
            wrddict[word]=1
    sortedwords=sorted(wrddict.items(),key=operator.itemgetter(1),reverse=True)



    return render(request,"count.html",{'k1_ft':ft,  'k2_wrdcount':len(wrdlist),  'k3_wrddict':wrddict,
    'k4_srt':sortedwords})


def vaboutfile(request):
    print('inside about file')
    return render(request,'about.html')
