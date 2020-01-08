from django.test import TestCase, Client, RequestFactory

from django.contrib.auth.models import AnonymousUser, User
from register.models import Profile, Transactions

from register.views import TransactionListView

class TestViews(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='Tom',
            email='tom@myspace.com',
            password='idm54875'
        )
        self.body = Transactions.objects


    def test_transaction_list_GET(self):
        request = self.factory.get('register:trans_list')
        request.user = self.user

        response = TransactionListView.as_view()(request)
        self.assertEquals(response.status_code, 200)

    def test_transaction_list_POST(self):
        data = {
            'title': 'My snippet',
            'content': 'This is my snippet'
        }

        request = self.factory.post('register:trans_list')
        request.user = self.user


        response = TransactionListView.as_view()(request)
        self.assertEquals(response.status_code, 302)
