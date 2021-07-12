from app.forms import LoginForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.test import SimpleTestCase
from django.urls import reverse,resolve
from app.views import add_to_cart, buy_now, orders, productView,productDetailView


#Adding Items To cart
class Test_add_o_cart_Urls(SimpleTestCase):
    def test_product(self):
        url=reverse('add-to-cart')
        print(resolve(url))
        self.assertEquals(resolve(url).func,add_to_cart)

class Test_buy_now_Urls(SimpleTestCase):
    def test_product(self):
        url=reverse('buy-now')
        print(resolve(url))
        self.assertEquals(resolve(url).func,buy_now)

class Test_orders_Urls(SimpleTestCase):
    def test_product(self):
        url=reverse('orders')
        print(resolve(url))
        self.assertEquals(resolve(url).func,orders)

"""class Test_Login_Urls(SimpleTestCase):
    def test_product(self):
        url=reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func)"""