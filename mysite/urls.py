from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),	
	path('register/',views.register,name="register"),
	path('shop/',views.shop,name="shop"),
	path('cartdetails/',views.cartdetails,name='cartdetails'),
    path('product-details/',views.productdetails,name='product-details'),
    path('checkout',views.checkout,name='checkout'),

]
