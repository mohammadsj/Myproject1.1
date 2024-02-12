from django.shortcuts import render
from django.http import HttpResponse
def home_view (reqouest):
    my = {'name':'Mohammad','lastname':'Sajadian','profession':'Python programmer','city' :'Shiraz',
          'instagram':'mohammad.sjr','telegram':'Mmmddow','github':'mohammadsj', 'vocation1':'Accounting',
          'vocation2': 'Python programmer', 'birthday':'2003 January 11','age':'21','phone':'+989392590527',
          'home':'marvdasht, iran','degree':'Start working', 'email':'mohammadsajadian3011@gmail.com',
          'text1':'I have been an accountant for 1 year. At the age of 13, I learned to repair mobile phones and at the age of 18, I started programming. I am currently a computer science student.',
          'address':'Iran,Shiraz,Marvdasht,Shahed Street'
          }
    return render(reqouest , 'index.html',my)
