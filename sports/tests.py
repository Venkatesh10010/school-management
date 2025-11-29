from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from sports.models import Sport
from django.contrib.auth.models import User


class SportAPITest(APITestCase):
    def setUp(self):
        # list url from router (basename='sport' -> 'sport-list')
        self.list_url = reverse('sport-list')   # -> /api/sports/

        # create one record to use for retrieve/update/delete tests
        self.s = Sport.objects.create(name="Football", description="Goal game")
        # helper to build detail URL for a pk
        self.detail_url = lambda pk: reverse('sport-detail', args=[pk])  # -> /api/sports/{pk}/

    def test_create_sport(self):
        """POST /api/sports/ creates sport and returns 201"""
        data = {"name": "Cricket", "description": "Bat and ball game"}
        resp = self.client.post(self.list_url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_get_sports(self):
        """GET /api/sports/ returns 200 OK"""
        resp = self.client.get(self.list_url, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_retrieve_sport_by_id(self):
        """GET /api/sports/{id}/ returns single record"""
        resp = self.client.get(self.detail_url(self.s.pk), format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['name'], 'Football')
        self.assertEqual(resp.data['description'], 'Goal game')

    def test_update_sport_put(self):
        """PUT /api/sports/{id}/ updates all fields and returns 200"""
        payload = {"name": "Football Modified", "description": "Updated description"}
        resp = self.client.put(self.detail_url(self.s.pk), payload, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        # refresh from DB and assert changes applied
        self.s.refresh_from_db()
        self.assertEqual(self.s.name, 'Football Modified')
        self.assertEqual(self.s.description, 'Updated description')

    def test_delete_sport(self):
        """DELETE /api/sports/{id}/ deletes record and returns 204"""
        resp = self.client.delete(self.detail_url(self.s.pk))
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
        # ensure DB record removed
        self.assertFalse(Sport.objects.filter(pk=self.s.pk).exists())


# class SportAuthAPITest(APITestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='venk', password='pass123')
#         self.list_url = reverse('sport-list')
#
#     def test_create_sport_auth(self):
#         self.client.force_authenticate(user=self.user)  #  user logged in
#         data = {"name": "Cricket", "description": "Bat and ball game"}
#         resp = self.client.post(self.list_url, data, format='json')
#         self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
