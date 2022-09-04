from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from cv2 import add
import jovian
import requests
from bs4 import BeautifulSoup
import pandas as pd
# Create your views here.

def home_page(request):
    return render(request, "home/index.html")
    #return HttpResponse("<h1>Hello World!</h1>")
def analytics_page(request):
    return render(request,"home/analytics.html")

def engineering(request):
    return render(request,"home/result.html")

def college_list(request):
    clg_india_url='https://collegedunia.com/btech-colleges'
    #request= requests.get(clg_india_url)
    header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36'}
    page=requests.get(clg_india_url,headers=header)


    selection_class = "jsx-2158881826 font-weight-bold text-md m-0"

    doc = BeautifulSoup(page.content, 'html.parser')

    clg_name = doc.find_all('h3', {'class': selection_class})

    fees_class_selection="jsx-2158881826 lr-key text-lg text-primary d-block font-weight-bold mb-1"
    fees=doc.find_all('span', {'class':fees_class_selection})

    course_name_class= 'jsx-2158881826 lr-value d-block mb-1'
    course_name=doc.find_all('span' , {'class':course_name_class})

    rating_class_selection='jsx-2158881826 rating-text text-white font-weight-bold text-base d-block text-right'
    rating=doc.find_all('span', {'class':rating_class_selection})

    address_class='jsx-2158881826 pr-1 location'
    address=doc.find_all('span',{'class':address_class})

    image_class='jsx-2158881826 img-overlay'   
    image=doc.find_all('div',{'class':image_class})
    #print(image[1].previous_sibling)

    print(len(clg_name),len(fees),len(image))

    parameter=[]
    index_for_fee=0


    for i in range(0,10):
        parameter_item={}
        parameter_item["College Name"]=clg_name[i].text
        parameter_item["BTECH"]=fees[index_for_fee].text
        parameter_item["EXAM"]=fees[index_for_fee+1].text
        parameter_item["Rating"]=fees[index_for_fee+2].text
        parameter_item["Address"]=address[i].text
        parameter_item['img']=image[i+2].previous_sibling['data-src']
        parameter.append(parameter_item)
        index_for_fee+=3
        

    top_colleges_df=pd.DataFrame(parameter)

    #print(parameter)

    top_colleges_df.to_csv('top_clgs.csv', index=None)

    df_new = pd.read_csv('top_clgs.csv')

    return JsonResponse(parameter,safe=False)