from django.test import TestCase
from contact.models import ContactEmail, ContactInfo


class ContactTestCase(TestCase):
    def setUp(self):
        ContactInfo.objects.create(address="test_address",
                                   phone_number="0777777778",
                                   email_address="test_email_address",
                                   facebook_link="test_facebook_link",
                                   instagram_link="test_instagram_link",
                                   telegram_link="test_telegram_link",
                                   twitter_link = "test_twitter_link",
                                   youtube_link="test_youtube_link",
                                   website="test_website",
                                   iframe_map="test_iframe_map",
                                   )

        ContactEmail.objects.create(name="test_email_user_name",
                                    email="test_email_value",
                                    message="test_email_message",
                                   )

    def test_contact_was_correctly_built(self):
        """Testing Contact-Model Object"""
        contact_information = ContactInfo.objects.get(address="test_address")
        contact_email = ContactEmail.objects.get(name="test_email_user_name")
        self.assertEqual(contact_information.phone_number, "0777777778")
        self.assertEqual(contact_email.email, "test_email_value")

