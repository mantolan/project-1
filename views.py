from django.shortcuts import render
from Myapplication.function import main_code
import multiprocessing
# Create your views here.
def home(request):
    return render(request,'index.html')
def main(request):
    return render(request,'main.html')
def recording(request):
    process = multiprocessing.Process(target=main_code)
    process.start()
    process.join()
    print("hello")
    return render(request,'main.html',{'content':'Listening'})
    