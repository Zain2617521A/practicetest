from django.shortcuts import render
from django.http import HttpResponse
from rango.models import News

# Create your views here.
def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by the number of likes in descending order.
    # Retrieve the top 5 only -- or all if less than 5.
    # Place the list in our context_dict dictionary (with our boldmessage!)
    # that will be passed to the template engine.
    news_list = News.objects.all()
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['news'] = news_list
    # Render the response and send it back!
    return render(request, 'rango/index.html', context=context_dict)
