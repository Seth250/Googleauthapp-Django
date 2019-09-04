from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from social_core.actions import do_complete
from social_django.utils import psa
from social_django.views import NAMESPACE, _do_login
from django.contrib.auth import REDIRECT_FIELD_NAME
...

@never_cache
@csrf_exempt
@psa('{0}:complete'.format(NAMESPACE))
def complete(request, backend, *args, **kwargs):
    """Authentication complete view"""
    return do_complete(request.backend, _do_login, user=None,
                       redirect_name = REDIRECT_FIELD_NAME, request = request,
                       *args, **kwargs)

def home(request):
	return render(request, 'home.html')
