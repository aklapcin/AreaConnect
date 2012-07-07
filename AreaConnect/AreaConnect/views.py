from AreaConnect.temp_users.models import RegisteredUser
from django.template import RequestContext
from django.shortcuts import render_to_response


def home(request, template="landing_page.html"):
    ctx = RequestContext(request)
    ctx['registered_email'] = None
    if request.method == 'POST':
        email = request.POST.get('email')
        postal_code = request.POST.get('postal_code')
        company_name = request.POST.get('company_name')
        user = RegisteredUser(email=email, company_name=company_name,\
            postal_code=postal_code)
        user.save()
        ctx['registered_email'] = email
    return render_to_response(template, {}, context_instance=ctx)
