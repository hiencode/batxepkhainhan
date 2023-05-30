from django.urls import path

from shop import views

app_name = "shop"

urlpatterns = [
	path('', views.home_page, name='home_page'),
    path('gioithieu', views.gioi_thieu, name='gioi_thieu'),
    path('lienhe', views.lien_he, name='lien_he'),
    path('cac_cong_trinh', views.cac_cong_trinh, name='cac_cong_trinh'),
    path('cong_trinh_que_toi', views.cong_trinh_que_toi, name='cong_trinh_que_toi'),
    path('cong_trinh_quan_ca_phe', views.cong_trinh_quan_ca_phe, name='cong_trinh_quan_ca_phe'),
    path('cong_trinh_nha_xuong', views.cong_trinh_nha_xuong, name='cong_trinh_nha_xuong'),
    path('cong_trinh_nha_pho', views.cong_trinh_nha_pho, name='cong_trinh_nha_pho'),
    path('mai_che_di_dong', views.mai_che_di_dong, name='mai_che_di_dong'),
    path('mai_hien_di_dong', views.mai_hien_di_dong, name='mai_hien_di_dong'),
	#path('<slug:slug>', views.product_detail, name='product_detail'),
	#path('add/favorites/<int:product_id>/', views.add_to_favorites, name='add_to_favorites'),
	#path('remove/favorites/<int:product_id>/', views.remove_from_favorites, name='remove_from_favorites'),
	#path('favorites/', views.favorites, name='favorites'),
	#path('search/', views.search, name='search'),
	#path('filter/<slug:slug>/', views.filter_by_category, name='filter_by_category'),
]