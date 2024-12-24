import os
import sys
import json
from http import HTTPStatus
import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from brp.historie_api.models.bad_request_foutbericht import (
    BadRequestFoutbericht,
)  # noqa: E501
from brp.historie_api.models.foutbericht import Foutbericht  # noqa: E501
from brp.historie_api.models.historie_query import HistorieQuery  # noqa: E501
from brp.historie_api.models.verblijfplaatshistorie_query_response import (
    VerblijfplaatshistorieQueryResponse,
)  # noqa: E501
from brp.historie_api import util

import brp_historie_client

import pprint

pp = pprint.PrettyPrinter(indent=4, stream=sys.stderr)

configuration = brp_historie_client.Configuration(
    host=os.getenv("BRP_HISTORIE_URL", "http://localhost"),
)


def verblijfplaatshistorie(historie_query=None):  # noqa: E501
    """verblijfplaatshistorie

    Raadpleeg de verblijfplaatshistorie van een persoon op de opgegeven peildatum of binnen de opgegeven periode. Het meest actuele adres staat bovenaan.  Zoek met burgerservicenummer  # noqa: E501

    :param historie_query:
    :type historie_query: dict | bytes

    :rtype: Union[VerblijfplaatshistorieQueryResponse, Tuple[VerblijfplaatshistorieQueryResponse, int], Tuple[VerblijfplaatshistorieQueryResponse, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        historie_query = HistorieQuery.from_dict(
            connexion.request.get_json()
        )  # noqa: E501

    # TODO: make this more direct than converting through JSON and back again
    try:
        historie_query = brp_historie_client.HistorieQuery.from_dict(
            connexion.request.get_json()
        )
    except Exception as e:
        return {
            "detail": str(e),
            "status": HTTPStatus.BAD_REQUEST,
            "title": str(type(e)),
        }, HTTPStatus.BAD_REQUEST

    with brp_historie_client.ApiClient(
        configuration=configuration,
        header_name="X-API-Key",
        header_value=os.getenv("BRP_HISTORIE_API_KEY", ""),
    ) as api_client:
        try:
            api_instance = brp_historie_client.BRPHistorieBevragenApi(api_client)
            api_response = api_instance.verblijfplaatshistorie(
                historie_query=historie_query
            )
            return api_response.to_dict(), HTTPStatus.OK
        except brp_historie_client.ApiException as ae:
            return json.loads(ae.body), ae.status
