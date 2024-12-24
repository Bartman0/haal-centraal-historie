import unittest

from flask import json

from brp.historie_api.models.bad_request_foutbericht import BadRequestFoutbericht  # noqa: E501
from brp.historie_api.models.foutbericht import Foutbericht  # noqa: E501
from brp.historie_api.models.historie_query import HistorieQuery  # noqa: E501
from brp.historie_api.models.verblijfplaatshistorie_query_response import VerblijfplaatshistorieQueryResponse  # noqa: E501
from brp.historie_api.test import BaseTestCase


class TestBRPHistorieBevragenController(BaseTestCase):
    """BRPHistorieBevragenController integration test stubs"""

    def test_verblijfplaatshistorie(self):
        """Test case for verblijfplaatshistorie

        
        """
        historie_query = {"burgerservicenummer":"555555021","type":"type"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/lap/api/brp/verblijfplaatshistorie',
            method='POST',
            headers=headers,
            data=json.dumps(historie_query),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
