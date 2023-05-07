import requests
from django.shortcuts import render,redirect
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from .models import Link

def scrape(request):
    if request.method=='POST':
        site=request.POST.get('site','')

        page = requests.get(site)
        soup = BeautifulSoup(page.text,'html.parser')
        # links=soup.find_all('a')

        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            Link.objects.create(address=link_address,name=link_text)
        return redirect('scrape')
    else:
        data = Link.objects.all()
    
    return render(request,'result.html',{'data':data})

def clear(request):
    Link.objects.all().delete()
    return redirect('scrape')