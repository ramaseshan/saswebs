from django.http import Http404
from django.shortcuts import render_to_response
import json
from django.http import HttpResponse
from django.db.models import Q

from sabwebs.models import product

def home(request,prod_id=None):
	products = product.objects.all()
	if prod_id is not None:
		# try:
		#     p = Poll.objects.get(pk=poll_id)
		# except Poll.DoesNotExist:
		#     raise Http404		
		p = product.objects.get(pid=prod_id)
		elevation = (p.p_price/100)*40
		max_elevation = p.p_price + elevation
		min_elevation = p.p_price - elevation
		related = product.objects.filter(
				Q(p_feature1__startswith=p.p_feature1) | Q(p_feature2__startswith=p.p_feature2) |
				Q(p_price__lte=max_elevation) , Q(p_price__gte=min_elevation)
			).exclude(pid=prod_id)[:10]
		return render_to_response('index.html', {'prod': p,'products':products,'related':related})
	else:
		return render_to_response('index.html',{'products':products})

def get_products(request):
	response_data = {}
	response_data['message'] = {"id": "1", "text": "option1"},{"id": "2", "text": "option2"},{"id": "3", "text": "option3"}
	return HttpResponse(json.dumps(response_data), content_type="application/json")
#[ {"id": "1", "text": "option1"},{"id": "2", "text": "option2"},{"id": "3", "text": "option3"} ]
