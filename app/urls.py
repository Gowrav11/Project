from app.forms import LoginForm
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm,MyPasswordResetForm,MySetPasswordForm

urlpatterns = [
    #path('', views.home),
    
    path('',views.productView.as_view(),name="home"),
    #product details
    path('product-detail/<int:pk>', views.productDetailView.as_view(), name='product-detail'),
    #Add to cart
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    #view cart
    path('cart/',views.show_cart,name='showcart'),
    path('pluscart/',views.plus_cart),
    path('minuscart/',views.minus_cart),
    path('removecart/',views.remove_cart),
    #buy
    path('buy/', views.buy_now, name='buy-now'),

    path('profile/', views.ProfileView.as_view(), name='profile'),


    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    


    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>',views.mobile,name='mobiledata'),


    #path('login/', views.login, name='login'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name='login'),

    #path('registration/', views.customerregistration, name='customerregistration'),
    path('registration/',views.CustomerRegistrationView.as_view(),name="customerregistration"),

    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),

    # password validation Methods
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',success_url='/passwordchangedone/',form_class=MyPasswordChangeForm),name='passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),name='password_reset_complete'),



    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
