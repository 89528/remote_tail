from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE
def button (request):
 #    ip = request.POST.get('ip')
  #   path = request.POST.get('path')
   return render(request, "index.html")
def external(request):
    ip = request.POST.get('ip')
    #path = request.POST.get('path')
    out = run(sys.executable,['//home//ashishmishra//Documents//python_code//show_date.py ',ip], shell=False, stdout=PIPE)
    #data=request.get()
    print(out)
   # data=data.text
    return render(request, "index.html", {'data':out.stdout})
