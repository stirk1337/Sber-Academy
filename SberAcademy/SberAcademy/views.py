from django.http import HttpResponseRedirect

def redirect(request):
    return HttpResponseRedirect('/test/browse')