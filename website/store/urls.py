from django.conf.urls.static import static
from django.urls import path
from .views import List_view, Detail_view, Create_user, SignUp, signout, add_to_cart, cart_product, delete_cart, order_user
from website import settings

urlpatterns = [
    path('', List_view.as_view(), name="product_list"),
    path('signup', Create_user.as_view(), name="signup"),
    path('signin', SignUp.as_view(), name="signin"),
    path('signout', signout, name="signout"),
    path('delete_cart', delete_cart, name="delete_cart"),
    path('cart_product', cart_product, name="cart_product"),
    path('order_user', order_user, name="order_user"),
    path('detail/<str:slug>', Detail_view.as_view(), name="product_detail"),
    path('add_to_cart/<str:slug>', add_to_cart, name="add_to_cart"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
