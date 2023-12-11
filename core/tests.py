from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Receipt


class ReceiptListViewTest(TestCase):

    def setUp(self) -> None:
        self.user1 = get_user_model().objects.create(username='user1')
        self.user1.set_password('user1')
        self.user1.save()

        self.user2 = get_user_model().objects.create(username='user2')
        self.user2.set_password('user2')
        self.user2.save()

        Receipt.objects.create(
            store_name='Store',
            date_of_purchase=timezone.now(),
            item_list='Item1 Item2',
            user=self.user1,
            total_amount=500)

        Receipt.objects.create(
            store_name='Store',
            date_of_purchase=timezone.now(),
            item_list='Item1 Item2',
            user=self.user1,
            total_amount=500)

        Receipt.objects.create(
            store_name='Store2',
            date_of_purchase=timezone.now(),
            item_list='Item1 Item2',
            user=self.user2,
            total_amount=500)

    def test_redirects_unauthenticated_users_to_login(self):
        response = self.client.get(reverse_lazy('receipt_list'))
        self.assertEquals(response.status_code, 302)

    def test_allows_authenticated_user(self):
        self.client.login(username='user1', password='user1')
        response = self.client.get(reverse_lazy('receipt_list'))
        self.assertEquals(response.status_code, 200)

    def test_displays_only_owned_receipts(self):
        self.client.login(username='user1', password='user1')
        response = self.client.get(reverse_lazy('receipt_list'))
        self.assertContains(response, 'user1')
        self.assertNotContains(response, 'user2')


class ReceiptDetailViewTest(TestCase):

    def setUp(self) -> None:
        self.user1 = get_user_model().objects.create(username='user1')
        self.user1.set_password('user1')
        self.user1.save()

        self.user2 = get_user_model().objects.create(username='user2')
        self.user2.set_password('user2')
        self.user2.save()

        self.user1_receipt = Receipt.objects.create(
            store_name='Store',
            date_of_purchase=timezone.now(),
            item_list='Item1 Item2',
            user=self.user1,
            total_amount=500)

        self.user2_receipt = Receipt.objects.create(
            store_name='Store2',
            date_of_purchase=timezone.now(),
            item_list='Item1 Item2',
            user=self.user2,
            total_amount=500)

    def test_redirects_unauthenticated_users_to_login(self):
        response = self.client.get(reverse_lazy(
            'receipt_detail', args=[self.user1_receipt.pk]))
        self.assertEquals(response.status_code, 302)

    def test_allows_owner(self):
        self.client.login(username='user1', password='user1')
        response = self.client.get(reverse_lazy(
            'receipt_detail', args=[self.user1_receipt.pk]))
        self.assertEquals(response.status_code, 200)

    def test_disallows_non_owner(self):
        self.client.login(username='user1', password='user1')
        response = self.client.get(reverse_lazy(
            'receipt_detail', args=[self.user2_receipt.pk]))
        self.assertEquals(response.status_code, 403)


class ReceiptUpdateViewTest(TestCase):

    def setUp(self) -> None:
        self.user1 = get_user_model().objects.create(username='user1')
        self.user1.set_password('user1')
        self.user1.save()

        self.user2 = get_user_model().objects.create(username='user2')
        self.user2.set_password('user2')
        self.user2.save()

        self.user1_receipt = Receipt.objects.create(
            store_name='Store',
            date_of_purchase=timezone.now(),
            item_list='Item1 Item2',
            user=self.user1,
            total_amount=500)

        self.user2_receipt = Receipt.objects.create(
            store_name='Store2',
            date_of_purchase=timezone.now(),
            item_list='Item1 Item2',
            user=self.user2,
            total_amount=500)

    def test_redirects_unauthenticated_users_to_login(self):
        response = self.client.get(reverse_lazy(
            'receipt_update', args=[self.user1_receipt.pk]))
        self.assertEquals(response.status_code, 302)

    def test_allows_owner(self):
        self.client.login(username='user1', password='user1')
        response = self.client.get(reverse_lazy(
            'receipt_update', args=[self.user1_receipt.pk]))
        self.assertEquals(response.status_code, 200)

    def test_disallows_non_owner(self):
        self.client.login(username='user1', password='user1')
        response = self.client.get(reverse_lazy(
            'receipt_update', args=[self.user2_receipt.pk]))
        self.assertEquals(response.status_code, 403)
