from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from shop.models import Product, Category
from cart.forms import QuantityForm


def paginat(request, list_objects):
	p = Paginator(list_objects, 20)
	page_number = request.GET.get('page')
	try:
		page_obj = p.get_page(page_number)
	except PageNotAnInteger:
		page_obj = p.page(1)
	except EmptyPage:
		page_obj = p.page(p.num_pages)
	return page_obj


def home_page(request):
	products = Product.objects.all()
	context = {'products': paginat(request ,products)}
	return render(request, 'home_page.html', context)

def gioi_thieu(request):
	products = Product.objects.all()
	context = {'products': paginat(request ,products)}
	return render(request, 'gioi_thieu.html', context)

def lien_he(request):
	products = Product.objects.all()
	context = {'products': paginat(request ,products)}
	return render(request, 'lien_he.html', context)

def bat_che(request):
	products = Product.objects.all()
	context = {'products': paginat(request ,products)}
	return render(request, 'bat_che.html', context)

def cac_cong_trinh(request):
	products = Product.objects.all()
	context = {'products': paginat(request ,products)}
	return render(request, 'cac_cong_trinh.html', context)

def cong_trinh_que_toi(request):
	products = Product.objects.all()
	context = {'products': paginat(request ,products)}
	return render(request, 'cong_trinh_que_toi.html', context)

def cong_trinh_quan_ca_phe(request):
	products = Product.objects.all()
	context = {'products': paginat(request ,products)}
	return render(request, 'cong_trinh_quan_ca_phe.html', context)

def cong_trinh_nha_xuong(request):
	products = Product.objects.all()
	context = {'products': paginat(request ,products)}
	return render(request, 'cong_trinh_nha_xuong.html', context)

def cong_trinh_nha_pho(request):
	products = Product.objects.all()
	context = {'products': paginat(request ,products)}
	return render(request, 'cong_trinh_nha_pho.html', context)

def cap_thep(request):
	products = Product.objects.all()
	context = {'products': paginat(request ,products)}
	return render(request, 'cap_thep.html', context)

def cap_thep(request):
	products = Product.objects.all()
	context = {'products': paginat(request ,products)}
	return render(request, 'cap_thep.html', context)

def du_che(request):
	products = Product.objects.all()
	context = {'products': paginat(request ,products)}
	return render(request, 'du_che.html', context)

def mai_che_di_dong(request):
	products = Product.objects.all()
	context = {'products': paginat(request ,products)}
	return render(request, 'mai_che_di_dong.html', context)

def mai_hien_di_dong(request):
	products = Product.objects.all()
	context = {'products': paginat(request ,products)}
	return render(request, 'mai_hien_di_dong.html', context)

def product_detail(request, slug):
	form = QuantityForm()
	product = get_object_or_404(Product, slug=slug)
	related_products = Product.objects.filter(category=product.category).all()[:5]
	context = {
		'title':product.title,
		'product':product,
		'form':form,
		'favorites':'favorites',
		'related_products':related_products
	}
	if request.user.likes.filter(id=product.id).first():
		context['favorites'] = 'remove'
	return render(request, 'product_detail.html', context)


@login_required
def add_to_favorites(request, product_id):
	product = get_object_or_404(Product, id=product_id)
	request.user.likes.add(product)
	return redirect('shop:product_detail', slug=product.slug)


@login_required
def remove_from_favorites(request, product_id):
	product = get_object_or_404(Product, id=product_id)
	request.user.likes.remove(product)
	return redirect('shop:favorites')


@login_required
def favorites(request):
	products = request.user.likes.all()
	context = {'title':'Favorites', 'products':products}
	return render(request, 'favorites.html', context)


def search(request):
	query = request.GET.get('q')
	products = Product.objects.filter(title__icontains=query).all()
	context = {'products': paginat(request ,products)}
	return render(request, 'home_page.html', context)


def filter_by_category(request, slug):
	"""when user clicks on parent category
	we want to show all products in its sub-categories too
	"""
	result = []
	category = Category.objects.filter(slug=slug).first()
	[result.append(product) \
		for product in Product.objects.filter(category=category.id).all()]
	# check if category is parent then get all sub-categories
	if not category.is_sub:
		sub_categories = category.sub_categories.all()
		# get all sub-categories products
		for category in sub_categories:
			[result.append(product) \
				for product in Product.objects.filter(category=category).all()]
	context = {'products': paginat(request ,result)}
	return render(request, 'home_page.html', context)
