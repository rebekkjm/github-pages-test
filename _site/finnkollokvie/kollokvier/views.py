from django.template import Context, loader, RequestContext
from kollokvier.models import Entry, EntryForm
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

def add(request):
    #c = {}
    e = EntryForm()
    c = {'entry': e}
    c.update(csrf(request))
    return render_to_response('kollokvier/add.html', c)

def list(request):
    try:
        if request.method=='POST':
            e = EntryForm(request.POST)
            new_entry = e.save()
    except ValueError:
        pass
    all_students_list = Entry.objects.all().order_by('-subject')
    #t = loader.get_template('kollokvier/list.html')
    #c = RequestContext({'all_students_list': all_students_list})
    #return HttpResponse(t.render(c))
    return render_to_response('kollokvier/list.html',{'all_students_list': all_students_list})
