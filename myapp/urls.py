from django.urls import path
from . import views

urlpatterns = [
   path('',views.index,name='index'),
   path('signup/', views.signup,name='signup'),
   path('login/',views.login,name='login'),
   path('logout/',views.logout,name='logout'),
   path('change_password/',views.change_password,name='change_password'),
   path('contact/',views.contact,name='contact'),
   path('send_otp/',views.send_otp,name='send_otp'),
   path('verify_otp/',views.verify_otp,name='verify_otp'),
   path('new_password/',views.new_password,name='new_password'),
   path('seller_index/',views.seller_index,name='seller_index'),
   path('seller_add_product/',views.seller_add_product,name='seller_add_product'),
   path('seller_view_product/',views.seller_view_product,name='seller_view_product'),
   path('seller_product_details/<int:pk>',views.seller_product_details,name='seller_product_details'),
   path('seller_edit_product/<int:pk>',views.seller_edit_product,name='seller_edit_product'),
   path('add_to_wishlist/<int:pk>/',views.add_to_wishlist,name='add_to_wishlist'),
   path('mywishlist/',views.mywishlist,name='mywishlist'),
   path('remove_from_wishlist/<int:pk>',views.remove_from_wishlist,name='remove_from_wishlist'),
   path('add_to_cart/<int:pk>/',views.add_to_cart,name='add_to_cart'),
   path('mycart/',views.mycart,name='mycart'),
   path('remove_from_cart/<int:pk>',views.remove_from_cart,name='remove_from_cart'),
   path('change_qty/<int:pk>/',views.change_qty,name='change_qty'),
   path('pay/',views.initiate_payment,name='pay'),
   path('callback/',views.callback, name='callback'),

]