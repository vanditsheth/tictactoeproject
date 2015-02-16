from django.shortcuts import render
from django.http import HttpResponse
from tictactoe.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import jinja2
from jinja2.ext import loopcontrols
from django.http import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

jinja_environ = jinja2.Environment(loader=jinja2.FileSystemLoader(['ui']), extensions=[loopcontrols])

def checker(moves):
    if (moves[6]==moves[7]==moves[8] and not moves[6]=="."):
        return '\nWinner is ' + moves[6]
    elif (moves[3]==moves[4]==moves[5] and not moves[3]=="."):
        return '\nWinner is ' + moves[3]
    elif (moves[0]==moves[1]==moves[2] and not moves[0]=="."):
        return '\nWinner is ' + moves[0]
    elif (moves[6]==moves[3]==moves[0] and not moves[6]=="."):
        return '\nWinner is ' + moves[6]
    elif (moves[7]==moves[4]==moves[1] and not moves[7]=="."):
        return '\nWinner is ' + moves[7]
    elif (moves[8]==moves[5]==moves[2] and not moves[8]=="."):
        return '\nWinner is ' + moves[8]
    elif (moves[6]==moves[4]==moves[2] and not moves[6]=="."):
        return '\nWinner is ' + moves[6]
    elif (moves[8]==moves[4]==moves[0] and not moves[8]=="."):
        return '\nWinner is ' + moves[8]
    elif '.' not in moves:
        return '\nThe game is tied. There are no winners.'
    else:
      return 0

def index(request):
  return HttpResponse(jinja_environ.get_template('index.html').render())

@csrf_exempt
def login_do(request):
    username = request.REQUEST['username']
    password = request.REQUEST['password']
    userthis = authenticate(username=username, password=password)
    if userthis is not None:
        if userthis.is_active:
            login(request, userthis)
            tmp=player.objects.get(user=userthis)
            movesarray=moves.objects.get(name="test")
	    return HttpResponse(jinja_environ.get_template('playboard.html').render({"turn":tmp.turn, "name":tmp.user.username, "moves":movesarray.moves}))

    else:
      return HttpResponse("Invalid Login. Go Back.")

def giveplayboardpage(request):
      tmp=player.objects.get(user=request.user.username)
      movesarray=moves.objects.get(name="test")
      return HttpResponse(jinja_environ.get_template('playboard.html').render({"turn":tmp.turn, "name":tmp.user.username, "moves":movesarray.moves}))

@csrf_exempt
def logout_do(request):
    logout(request)
    return HttpResponse(jinja_environ.get_template('index.html').render())
  
@csrf_exempt
def refresh(request):
    tmp=player.objects.get(name=request.user.username)
    movesarray=moves.objects.get(name="test")
    return HttpResponse(jinja_environ.get_template('playboard.html').render({"turn":tmp.turn, "name":tmp.user.username, "moves":movesarray.moves}))
    
 
@csrf_exempt
def playturn(request):
    playert=request.user.username
    cellnumber = request.REQUEST['cellnumber']
    movesarray=moves.objects.get(name="test")
    
    if int(cellnumber) not in [1,2,3,4,5,6,7,8,9]:
      return HttpResponse("Invalid Number. Go Back and enter again")
    
    if not movesarray.moves[int(cellnumber)-1] == ".":
      return HttpResponse("Enter Only on empty cells. Go Back and enter again")
    
    if playert=='cross':
      movesarray.moves=movesarray.moves[0:int(cellnumber)-1]+'x'+movesarray.moves[int(cellnumber):]
      movesarray.save()
      
      playerobj=player.objects.get(name='cross')
      if playerobj.turn==1:
	playerobj.turn=0
      elif playerobj.turn==0:
	playerobj.turn=1
      playerobj.save()

      playerobj=player.objects.get(name='zero')
      if playerobj.turn==1:
	playerobj.turn=0
      elif playerobj.turn==0:
	playerobj.turn=1
      playerobj.save()

      tmp=player.objects.get(name='cross')
      
    elif playert=='zero':
      movesarray.moves=movesarray.moves[0:int(cellnumber)-1]+'o'+movesarray.moves[int(cellnumber):]
      movesarray.save()

      playerobj=player.objects.get(name='zero')      
      if playerobj.turn==1:
	playerobj.turn=0
      elif playerobj.turn==0:
	playerobj.turn=1      
      playerobj.save()

      playerobj=player.objects.get(name='cross')
      if playerobj.turn==1:
	playerobj.turn=0
      elif playerobj.turn==0:
	playerobj.turn=1
      playerobj.save()

      tmp=player.objects.get(name='zero')
      
    movesarray=moves.objects.get(name='test')
    
    checkervar=checker(movesarray.moves)
    
    if checkervar==0:
      return HttpResponse(jinja_environ.get_template('playboard.html').render({"turn":tmp.turn, "name":tmp.user.username, "moves":movesarray.moves}))
    else:
      arr=[]
      arr=movesarray.moves
      movesarray.moves='.........'
      movesarray.save()
      return HttpResponse(jinja_environ.get_template('end.html').render({"message":checkervar, "moves":arr}))