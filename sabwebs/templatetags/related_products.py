from django import template
from django.db.models import Q
from sabwebs.models import product

register = template.Library()
# The first argument *must* be called "context" here.
def related(context,prod_id):
	prod = product.objects.get(pid=prod_id)
	elevation = (prod.p_price/40)
	max_elevation = prod.p_price + elevation
	min_elevation = prod.p_price - elevation

	related = product.objects.filter(p_price__lte = max_elevation,p_price__gte = min_elevation)
	#r_products = product.objects.filter(p_price <= prod.p_price,p_price>=)
	return {
		#'link': context['home_link'],
		'hello':'hello',
		'related':related
	}

# Register the custom tag as an inclusion tag with takes_context=True.
register.inclusion_tag('related_products.html', takes_context=True)(related)


#08025579500