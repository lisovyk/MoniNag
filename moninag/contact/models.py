"""This module contains Contact model class and basic functions"""

from django.db import models

from registration.models import CustomUser


class Contact(models.Model):
    """
    Contact
    :argument id: int - autogenerated primary key
    :argument first_name: str - Contact first name
    :argument second_name: str - Contact second name
    :argument email: str - Contact email
    :argument is_active: bool - Contact state
    :argument activation_key: str - Contact activation key
    :argument user: str - CustomUser id - user owner id
    """

    first_name = models.CharField(max_length=200, blank=None)
    second_name = models.CharField(max_length=200, blank=None)
    email = models.EmailField(blank=False, unique=True)
    is_active = models.BooleanField(default=False)
    activation_key = models.CharField(default='', max_length=1000, editable=False)
    user = models.ForeignKey(CustomUser)

    def update(self, first_name=None, second_name=None, email=None):
        """Update contact data.
        :param first_name: str - contact first name
        :param second_name: str - contact second name
        :param email: str - contact email
        """

        if first_name:
            self.first_name = first_name
        if second_name:
            self.second_name = second_name
        if email:
            self.email = email

        self.save()

    @staticmethod
    def get_by_id(contact_id):
        """
        :param contact_id: int - contact id
        :return: Object<Contact>: Object of contact.
        """

        try:
            contact = Contact.objects.get(id=contact_id)
            return contact
        except Contact.DoesNotExist:
            return None

    @staticmethod
    def get_by_user_id(user_id):
        """
        :param user_id: int - user id
        :return: QuerySet<Contact>: QuerySet of contacts.
        """
        return Contact.objects.filter(user=user_id)

    @staticmethod
    def get_by_email(email):
        """
        :param email: str - contact email
        :return: Object<Contact>: Object of contact.
        """
        try:
            contact = Contact.objects.get(email=email)
            return contact
        except Contact.DoesNotExist:
            return None

    def to_dict(self):
        """Convert model object to dictionary.

        :return: dict:
                {
                    'id': contact id,
                    'first_name': first name,
                    'second_name': second name,
                    'email': email,
                    'is_active': contact status.
                }
        """

        return {
            'id': self.id,
            'first_name': self.first_name,
            'second_name': self.second_name,
            'email': self.email,
            'is_active': self.is_active
        }
