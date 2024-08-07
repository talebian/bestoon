from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from web.models import User, Token, Expense, Income
import datetime
# Create your views here.

def submit_expense(request):
    """ submit an expense """

    #TODO: validate data, user might be fake, token might be fake, amount might be...
    this_token = request.GET['token']
    this_user = User.objects.filter(token__token = this_token).get()
    if 'date' not in request.GET:
        date = datetime.datetime.now() 
    Expense.objects.create(user = this_user, amount = request.GET['amount'],
                           text = request.GET['text'], date = date)

    print("I'm in submit expense with POST method. The request.POST is", request.POST)
    print("While the request.GET is", request.GET)


    return JsonResponse({
        'status': 'ok > GET method'
    }, encoder=JSONEncoder)