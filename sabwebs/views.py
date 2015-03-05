from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
import json
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User

from sabwebs.models import product,prod_user
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.models import User

@login_required
def home(request,prod_id=None):
	products = product.objects.all()
	if prod_id is not None:
		# try:
		#     p = Poll.objects.get(pk=poll_id)
		# except Poll.DoesNotExist:
		#     raise Http404		
		p = product.objects.get(pid=prod_id)
		elevation = (p.p_price/100)*20
		max_elevation = p.p_price + elevation
		min_elevation = p.p_price - elevation
                userliked = prod_user.objects.filter(uid=request.user.id)
                liked_prod = product.objects.filter(
				Q(p_feature1__startswith=p.p_feature1) | Q(p_feature2__startswith=p.p_feature2) |
				Q(p_price__lte=max_elevation) , Q(p_price__gte=min_elevation), pid__in=prod_user.objects.filter(uid=request.user.id)
			).exclude(pid=prod_id)[:10]
                print liked_prod
		related = product.objects.filter(
				Q(p_feature1__startswith=p.p_feature1) | Q(p_feature2__startswith=p.p_feature2) |
				Q(p_price__lte=max_elevation) , Q(p_price__gte=min_elevation)
			).exclude(Q(pid__in=prod_user.objects.filter(uid=request.user.id))| Q(pid=prod_id))[:20]
                print related
		return render_to_response('index.html', {'prod': p,'products':products,'liked_prod':liked_prod,'related':related})
	else:
		return render_to_response('index.html',{'products':products})

@csrf_exempt
def do_like(request):
        pid = request.POST.get('pid').split('_')[1]
        prod = product.objects.get(pid=pid)
        user = User.objects.get(id=request.user.id)
        clicked = prod_user.objects.create(uid=user,pid=prod,nclick=1)
        clicked.save()
        return HttpResponse("Success")
@csrf_exempt
def undo_like(request):
        pid = request.POST.get('pid').split('_')[1]
        prod = product.objects.get(pid=pid)
        user = User.objects.get(id=request.user.id)
        clicked = prod_user.objects.filter(uid=user,pid=prod)
        print clicked
        clicked.delete()
        return HttpResponse("Success")

def get_products(request):
	response_data = {}
	response_data['message'] = {"id": "1", "text": "option1"},{"id": "2", "text": "option2"},{"id": "3", "text": "option3"}
	return HttpResponse(json.dumps(response_data), content_type="application/json")
#[ {"id": "1", "text": "option1"},{"id": "2", "text": "option2"},{"id": "3", "text": "option3"} ]
