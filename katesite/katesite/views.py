import datetime
from django.http import HttpResponse
from django.template import Context, loader

# def home(request):
#     
#     now = datetime.datetime.now()
#     html = "<html><body>The time is now %s.</body></html>" % now
#     return HttpResponse(html)
    
def home(request):
    template = loader.get_template('base.html')
    context = Context()
    return HttpResponse(template.render(context))