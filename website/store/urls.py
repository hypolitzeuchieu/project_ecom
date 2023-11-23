from django.conf.urls.static import static
from django.urls import path
from .views import List_view, Detail_view, Create_user, SignUp, signout
from website import settings

urlpatterns = [
    path('', List_view.as_view(), name="product_list"),
    path('detail/<str:slug>', Detail_view.as_view(), name="product_detail"),
    path('signup', Create_user.as_view(), name="signup"),
    path('signin', SignUp.as_view(), name="signin"),
    path('signout', signout, name="signout"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)