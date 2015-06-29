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

@csrf_exempt
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
      	    if username=='aarushi':
	      return HttpResponse(jinja_environ.get_template('specialpage.html').render({}))

      	    if username=='agnes':
	      return HttpResponse(jinja_environ.get_template('HTML/Welcome.html').render({}))

	    tmp=player.objects.get(name=username)
	    movesarray=moves.objects.get(name="test")
	    p1=movesarray.player1
	    p2=movesarray.player2
	    
	    tmpmessagearr=messages.objects.filter()
	    messagearr=messages.objects.filter().order_by('-id')[:12][::-1]
	    diffarr=[aa for aa in tmpmessagearr if aa not in messagearr]
	    for i in diffarr:
	      i.delete()

	    if p1==p2==4:
	      p1==0
	      p2==0
	      movesarray.save()

	    if p1==0 and p2==0:
	      return HttpResponse(jinja_environ.get_template('playboard.html').render({"turn":tmp.turn, "name":tmp.user.username, "moves":movesarray.moves, "messagearr":messagearr}))

	    elif tmp.name=='cross':
	      if p1==1:
		return HttpResponse(jinja_environ.get_template('end.html').render({"message":'Winner is x', "moves":movesarray.moves}))
	      elif p1==2:
		return HttpResponse(jinja_environ.get_template('end.html').render({"message":'Winner is o', "moves":movesarray.moves}))
	      elif p1==3:
		return HttpResponse(jinja_environ.get_template('end.html').render({"message":'Game has been tied', "moves":movesarray.moves}))
	      elif p1==4:
		return HttpResponse(jinja_environ.get_template('waitplayer.html').render({"message":'Please wait for other player to press play again', "moves":movesarray.moves}))

	    elif tmp.name=='zero':
	      if p2==1:
		return HttpResponse(jinja_environ.get_template('end.html').render({"message":'Winner is x', "moves":movesarray.moves}))
	      elif p2==2:
		return HttpResponse(jinja_environ.get_template('end.html').render({"message":'Winner is o', "moves":movesarray.moves}))
	      elif p2==3:
		return HttpResponse(jinja_environ.get_template('end.html').render({"message":'Game has been tied', "moves":movesarray.moves}))
	      elif p2==4:
		return HttpResponse(jinja_environ.get_template('waitplayer.html').render({"message":'Please wait for other player to press play again', "moves":movesarray.moves}))
	      
    else:
      return HttpResponse("Invalid Login. Go Back.")

@csrf_exempt
def giveplayboardpage(request):
      tmp=player.objects.get(name=request.user.username)
      movesarray=moves.objects.get(name="test")
      
      tmpmessagearr=messages.objects.filter()
      messagearr=messages.objects.filter().order_by('-id')[:12][::-1]
      diffarr=[aa for aa in tmpmessagearr if aa not in messagearr]
      for i in diffarr:
	i.delete()


      if tmp.name=='cross':
	movesarray.player1=4
	movesarray.save()
      else:
	movesarray.player2=4
	movesarray.save()

      if movesarray.player1==movesarray.player2==4:
	movesarray.player1=0
	movesarray.player2=0
	movesarray.moves='.........'
	movesarray.save()
	return HttpResponse(jinja_environ.get_template('playboard.html').render({"turn":tmp.turn, "name":tmp.user.username, "moves":movesarray.moves, "messagearr":messagearr}))

      elif tmp.name=='cross' and movesarray.player2!=4:
	return HttpResponse(jinja_environ.get_template('waitplayer.html').render({"message":'Please wait for other player to press play again', "moves":movesarray.moves}))

      elif tmp.name=='zero' and movesarray.player1!=4:
	return HttpResponse(jinja_environ.get_template('waitplayer.html').render({"message":'Please wait for other player to press play again', "moves":movesarray.moves}))
	

@csrf_exempt
def logout_do(request):
    logout(request)
    return HttpResponse(jinja_environ.get_template('index.html').render())
  
@csrf_exempt
def refresh(request):
    tmp=player.objects.get(name=request.user.username)
    movesarray=moves.objects.get(name="test")
    p1=movesarray.player1
    p2=movesarray.player2
    
    tmpmessagearr=messages.objects.filter()
    messagearr=messages.objects.filter().order_by('-id')[:12][::-1]
    diffarr=[aa for aa in tmpmessagearr if aa not in messagearr]
    for i in diffarr:
      i.delete()


    if p1==p2==4:
      p1==0
      p2==0
      movesarray.save()

    if p1==0 and p2==0:
      return HttpResponse(jinja_environ.get_template('playboard.html').render({"turn":tmp.turn, "name":tmp.user.username, "moves":movesarray.moves, "messagearr":messagearr}))

    elif tmp.name=='cross':
      if p1==1:
	return HttpResponse(jinja_environ.get_template('end.html').render({"message":'Winner is x', "moves":movesarray.moves}))
      elif p1==2:
      	return HttpResponse(jinja_environ.get_template('end.html').render({"message":'Winner is o', "moves":movesarray.moves}))
      elif p1==3:
	return HttpResponse(jinja_environ.get_template('end.html').render({"message":'Game has been tied', "moves":movesarray.moves}))
      elif p1==4:
	return HttpResponse(jinja_environ.get_template('waitplayer.html').render({"message":'Please wait for other player to press play again', "moves":movesarray.moves}))

    elif tmp.name=='zero':
      if p2==1:
	return HttpResponse(jinja_environ.get_template('end.html').render({"message":'Winner is x', "moves":movesarray.moves}))
      elif p2==2:
      	return HttpResponse(jinja_environ.get_template('end.html').render({"message":'Winner is o', "moves":movesarray.moves}))
      elif p2==3:
	return HttpResponse(jinja_environ.get_template('end.html').render({"message":'Game has been tied', "moves":movesarray.moves}))
      elif p2==4:
	return HttpResponse(jinja_environ.get_template('waitplayer.html').render({"message":'Please wait for other player to press play again', "moves":movesarray.moves}))
 
@csrf_exempt
def playturn(request):
    playert=request.user.username
    cellnumber = request.REQUEST['cellnumber']
    movesarray=moves.objects.get(name="test")
    
    tmpmessagearr=messages.objects.filter()
    messagearr=messages.objects.filter().order_by('-id')[:12][::-1]
    diffarr=[aa for aa in tmpmessagearr if aa not in messagearr]
    for i in diffarr:
      i.delete()

    
    if cellnumber not in ['1','2','3','4','5','6','7','8','9']:
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
      return HttpResponse(jinja_environ.get_template('playboard.html').render({"turn":tmp.turn, "name":tmp.user.username, "moves":movesarray.moves, "p1":movesarray.player1, "p2":movesarray.player2, "messagearr":messagearr}))
    
    elif 'Winner' in checkervar:
      if 'x' in checkervar:
	movesarray.player1=1
	movesarray.player2=1
	movesarray.save()
      else:
	movesarray.player1=2
	movesarray.player2=2
	movesarray.save()
      return HttpResponse(jinja_environ.get_template('end.html').render({"message":checkervar, "moves":movesarray.moves}))
    
    else:
      movesarray.player1=3
      movesarray.player2=3
      movesarray.save()
      return HttpResponse(jinja_environ.get_template('end.html').render({"message":checkervar, "moves":movesarray.moves}))

def displaymessages(request):
   
   return HttpResponse(jinja_environ.get_template('testfile.html').render({"messagearr":messagearr}))

@csrf_exempt
def sendmessage(request):
    name=request.user.username
    text = request.REQUEST['text']
    newmessage = messages(sender=name, message=text)
    newmessage.save()

    tmp=player.objects.get(name=name)
    movesarray=moves.objects.get(name="test")
    p1=movesarray.player1
    p2=movesarray.player2
    
    tmpmessagearr=messages.objects.filter()
    messagearr=messages.objects.filter().order_by('-id')[:12][::-1]
    diffarr=[aa for aa in tmpmessagearr if aa not in messagearr]
    for i in diffarr:
      i.delete()


    if p1==p2==4:
      p1==0
      p2==0
      movesarray.save()

    if p1==0 and p2==0:
      return HttpResponse(jinja_environ.get_template('playboard.html').render({"turn":tmp.turn, "name":tmp.user.username, "moves":movesarray.moves, "messagearr":messagearr}))

    elif tmp.name=='cross':
      if p1==1:
	return HttpResponse(jinja_environ.get_template('end.html').render({"message":'Winner is x', "moves":movesarray.moves}))
      elif p1==2:
      	return HttpResponse(jinja_environ.get_template('end.html').render({"message":'Winner is o', "moves":movesarray.moves}))
      elif p1==3:
	return HttpResponse(jinja_environ.get_template('end.html').render({"message":'Game has been tied', "moves":movesarray.moves}))
      elif p1==4:
	return HttpResponse(jinja_environ.get_template('waitplayer.html').render({"message":'Please wait for other player to press play again', "moves":movesarray.moves}))

    elif tmp.name=='zero':
      if p2==1:
	return HttpResponse(jinja_environ.get_template('end.html').render({"message":'Winner is x', "moves":movesarray.moves}))
      elif p2==2:
      	return HttpResponse(jinja_environ.get_template('end.html').render({"message":'Winner is o', "moves":movesarray.moves}))
      elif p2==3:
	return HttpResponse(jinja_environ.get_template('end.html').render({"message":'Game has been tied', "moves":movesarray.moves}))
      elif p2==4:
	return HttpResponse(jinja_environ.get_template('waitplayer.html').render({"message":'Please wait for other player to press play again', "moves":movesarray.moves}))

    