from django.shortcuts import render
from .models import Question, Choice, Booking, Conv


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    global cid
    if request.method == 'POST':
            chat = request.POST.get('question')
            question = Question.objects.all()
            for i in range(len(question)):
                if(str(question[i])==chat):
                    c = '\r\nquestion: {}'.format(question[i])
            if (chat == None):
                chat = request.POST.get('answer')
                c = '\r\nanswer: {}'.format(chat)
            try:
                con = Conv.objects.get(id=cid).conv
                if c in con:
                    conver = con
                else:
                    conver = con + c
            except:
                conver = c
            Conv.objects.filter(id=cid).update(conv=conver)
            que = []
            ans = []
            for i in range(len(con.split('\r\n'))):
                    if con.split('\r\n')[i].split(':')[0] == 'question':
                        queno = con.split('\r\n')[i].split(':')[1]
                        que.append((queno))
                    else:
                        ansres = con.split('\r\n')[i].split(':')[1]
                        ans.append(ansres)
            chat = zip(que, ans)
            q = []
            for i in range(len(que) - 1, len(question)):
                if question[i] in que:
                    pass
                else:
                    nxtque = question[i]
                    q.append(nxtque)
            return render(request, 'chat/room.html', {'questions': q,'chat': chat,})
    else:
        try:
            user = Conv.objects.get(user = room_name)
            cid = user.id
            con = user.conv
            choice = Choice.objects.all()
            question = Question.objects.all()
            que = []
            ans = []
            try:
                for i in range(len(con.split('\r\n'))):
                    if con.split('\r\n')[i].split(':')[0] == 'question':
                        queno = con.split('\r\n')[i].split(':')[1]
                        que.append(queno)
                    else:
                        ansres = con.split('\r\n')[i].split(':')[1]
                        ans.append(ansres)
                if len(que) == len(ans):
                        pass
                else:
                        r=con
                        s = r.replace(con.split('\r\n')[len(con.split('\r\n'))-1], '')
                        m = s.rstrip()
                        Conv.objects.filter(id=cid).update(conv=m)
                        user.conv
                chat = zip(que, ans)
                q = []
                for i in range(len(que)-1,len(question)):
                    if ' {}'.format(question[i]) in que:
                        pass
                    else:
                        nxtque = question[i]
                        q.append(nxtque)
                return render(request, 'chat/room.html', {'questions': q,'chat': chat, 'choice': choice})
            except:
                return render(request, 'chat/room.html',{'questions': question,'choice': choice})
        except:
            chat = Conv(user=room_name)
            # chat.save()
            cid = chat.id
            question = Question.objects.all()
            choice = Choice.objects.all()
            request.session['user'] = room_name
            return render(request, 'chat/room.html', {
                'room_name': room_name, 'questions': question, 'choice': choice
            })

