from django.test import SimpleTestCase
from django.urls import reverse, resolve
from register.views import TransactionListView, TransactionDeleteView, LegendCodeListView, LegendCodeDeleteView

class TestUrls(SimpleTestCase):

    def test_trans_list_url_is_resolve(self):
        url = reverse('register:trans_list')
        self.assertEquals(resolve(url).func.view_class, TransactionListView)

    def test_trans_delete_url_is_resolve(self):
        url = reverse('register:tran_del', args=[1])
        self.assertEquals(resolve(url).func.view_class, TransactionDeleteView)

    def test_legend_list_url_is_resolve(self):
        url = reverse('register:legend_code_list')
        self.assertEquals(resolve(url).func.view_class, LegendCodeListView)

    def test_legend_code_delete_url_is_resolve(self):
        url = reverse('register:code_del', args=[1])
        self.assertEquals(resolve(url).func.view_class, LegendCodeDeleteView)
