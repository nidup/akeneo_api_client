# -*- coding: utf-8 -*-

from akeneo_api_client.utils import *
from akeneo_api_client.interfaces import *
from akeneo_api_client.auth import *
from akeneo_api_client.resources import *
import requests
import json

import logging
import logzero
from logzero import logger

import urllib.parse


class Client:
    BASIC_API_PATH = '/api/rest/v1/'
    RESOURCE_NAMES = [
        'association_types', 
        'attributes', 
        'attribute_groups',
        'categories', 
        'channels', 
        'currencies', 
        'families', 
        'locales', 
        'measure_families',
        'media_files',
        'products',
        'product_models'
    ]

    def __init__(self,
        base_url, client_id=None, secret=None, username=None, password=None,
        session=None, auth=None):
        """Expect credential
        1) as auth, or 
        2) as client_id+secret+username+password, or
        3) as session having an authentication."""
        provided_auth = False
        if not auth:
            if client_id or secret or username or password:
                if client_id and secret and username and password:
                    provided_auth = True
                    auth = Auth(base_url, client_id, secret, 
                                username, password)
            elif session:
                provided_auth = True
        else:
            provided_auth = True
        if not provided_auth:
            raise ValueError("Expect credential 1) as auth, or "
                           + "2) as client_id+secret+username+password, or "
                           + "3) as session having an authentication.")
        if not session:
            session = requests.Session()
        self._init(base_url, session, auth)

    def _init(self, base_url, session, auth):
        self._base_url = base_url
        self._session = session
        if auth:
            self._session.auth = auth
        self._session.headers.update({'Content-Type': 'application/json'})
        self._association_types = ResourcePool(
            urljoin(self._base_url, self.BASIC_API_PATH, 'association-types/'), session)
        self._attributes = ResourcePool(
            urljoin(self._base_url, self.BASIC_API_PATH, 'attributes/'), session)
        self._attribute_groups = ResourcePool(
            urljoin(self._base_url, self.BASIC_API_PATH, 'attribute-groups/'), session)
        self._categories = ResourcePool(
            urljoin(self._base_url, self.BASIC_API_PATH, 'categories/'), session)
        self._channels = ResourcePool(
            urljoin(self._base_url, self.BASIC_API_PATH, 'channels/'), session)
        self._currencies = ResourcePool(
            urljoin(self._base_url, self.BASIC_API_PATH, 'currencies/'), session)
        self._families = ResourcePool(
            urljoin(self._base_url, self.BASIC_API_PATH, 'families/'), session)
        self._locales = ResourcePool(
            urljoin(self._base_url, self.BASIC_API_PATH, 'locales/'), session)
        self._measure_families = ResourcePool(
            urljoin(self._base_url, self.BASIC_API_PATH, 'measure-families/'), session)
        self._media_files = ResourcePool(
            urljoin(self._base_url, self.BASIC_API_PATH, 'media-files/'), session)
        self._products = ResourcePool(
            urljoin(self._base_url, self.BASIC_API_PATH, 'products/'), session)
        self._product_models = ResourcePool(
            urljoin(self._base_url, self.BASIC_API_PATH, 'product-models/'), session)

    @property
    def association_types(self):
        return self._association_types
    @property
    def attributes(self):
        return self._attributes
    @property
    def attribute_groups(self):
        return self._attribute_groups
    @property
    def categories(self):
        return self._categories
    @property
    def channels(self):
        return self._channels
    @property
    def currencies(self):
        return self._currencies
    @property
    def families(self):
        return self._families
    @property
    def locales(self):
        return self._locales
    @property
    def measure_families(self):
        return self._measure_families
    @property
    def media_files(self):
        return self._media_files
    @property
    def products(self):
        return self._products
    @property
    def product_models(self):
        return self._product_models