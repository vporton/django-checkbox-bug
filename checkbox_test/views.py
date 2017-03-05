from django.http import HttpResponse
import checkbox_test.forms

def test(request):
    return HttpResponse(str(checkbox_test.forms.MyForm()))