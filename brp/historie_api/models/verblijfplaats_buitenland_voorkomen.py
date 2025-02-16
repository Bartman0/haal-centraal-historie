from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from brp.historie_api.models.base_model import Model
from brp.historie_api.models.abstract_datum import AbstractDatum
from brp.historie_api.models.abstract_verblijfplaats_voorkomen import AbstractVerblijfplaatsVoorkomen
from brp.historie_api.models.adressering_buitenland import AdresseringBuitenland
from brp.historie_api.models.rni_deelnemer import RniDeelnemer
from brp.historie_api.models.verblijfadres_buitenland import VerblijfadresBuitenland
from brp.historie_api.models.verblijfplaats_buitenland_voorkomen_in_onderzoek import VerblijfplaatsBuitenlandVoorkomenInOnderzoek
from brp.historie_api.models.waardetabel import Waardetabel
from brp.historie_api import util

from brp.historie_api.models.abstract_datum import AbstractDatum  # noqa: E501
from brp.historie_api.models.abstract_verblijfplaats_voorkomen import AbstractVerblijfplaatsVoorkomen  # noqa: E501
from brp.historie_api.models.adressering_buitenland import AdresseringBuitenland  # noqa: E501
from brp.historie_api.models.rni_deelnemer import RniDeelnemer  # noqa: E501
from brp.historie_api.models.verblijfadres_buitenland import VerblijfadresBuitenland  # noqa: E501
from brp.historie_api.models.verblijfplaats_buitenland_voorkomen_in_onderzoek import VerblijfplaatsBuitenlandVoorkomenInOnderzoek  # noqa: E501
from brp.historie_api.models.waardetabel import Waardetabel  # noqa: E501

class VerblijfplaatsBuitenlandVoorkomen(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, verblijfadres=None, datum_van=None, datum_tot=None, gemeente_van_inschrijving=None, in_onderzoek=None, rni=None, adressering=None):  # noqa: E501
        """VerblijfplaatsBuitenlandVoorkomen - a model defined in OpenAPI

        :param type: The type of this VerblijfplaatsBuitenlandVoorkomen.  # noqa: E501
        :type type: str
        :param verblijfadres: The verblijfadres of this VerblijfplaatsBuitenlandVoorkomen.  # noqa: E501
        :type verblijfadres: VerblijfadresBuitenland
        :param datum_van: The datum_van of this VerblijfplaatsBuitenlandVoorkomen.  # noqa: E501
        :type datum_van: AbstractDatum
        :param datum_tot: The datum_tot of this VerblijfplaatsBuitenlandVoorkomen.  # noqa: E501
        :type datum_tot: AbstractDatum
        :param gemeente_van_inschrijving: The gemeente_van_inschrijving of this VerblijfplaatsBuitenlandVoorkomen.  # noqa: E501
        :type gemeente_van_inschrijving: Waardetabel
        :param in_onderzoek: The in_onderzoek of this VerblijfplaatsBuitenlandVoorkomen.  # noqa: E501
        :type in_onderzoek: VerblijfplaatsBuitenlandVoorkomenInOnderzoek
        :param rni: The rni of this VerblijfplaatsBuitenlandVoorkomen.  # noqa: E501
        :type rni: RniDeelnemer
        :param adressering: The adressering of this VerblijfplaatsBuitenlandVoorkomen.  # noqa: E501
        :type adressering: AdresseringBuitenland
        """
        self.openapi_types = {
            'type': str,
            'verblijfadres': VerblijfadresBuitenland,
            'datum_van': AbstractDatum,
            'datum_tot': AbstractDatum,
            'gemeente_van_inschrijving': Waardetabel,
            'in_onderzoek': VerblijfplaatsBuitenlandVoorkomenInOnderzoek,
            'rni': RniDeelnemer,
            'adressering': AdresseringBuitenland
        }

        self.attribute_map = {
            'type': 'type',
            'verblijfadres': 'verblijfadres',
            'datum_van': 'datumVan',
            'datum_tot': 'datumTot',
            'gemeente_van_inschrijving': 'gemeenteVanInschrijving',
            'in_onderzoek': 'inOnderzoek',
            'rni': 'rni',
            'adressering': 'adressering'
        }

        self._type = type
        self._verblijfadres = verblijfadres
        self._datum_van = datum_van
        self._datum_tot = datum_tot
        self._gemeente_van_inschrijving = gemeente_van_inschrijving
        self._in_onderzoek = in_onderzoek
        self._rni = rni
        self._adressering = adressering

    @classmethod
    def from_dict(cls, dikt) -> 'VerblijfplaatsBuitenlandVoorkomen':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VerblijfplaatsBuitenlandVoorkomen of this VerblijfplaatsBuitenlandVoorkomen.  # noqa: E501
        :rtype: VerblijfplaatsBuitenlandVoorkomen
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this VerblijfplaatsBuitenlandVoorkomen.


        :return: The type of this VerblijfplaatsBuitenlandVoorkomen.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this VerblijfplaatsBuitenlandVoorkomen.


        :param type: The type of this VerblijfplaatsBuitenlandVoorkomen.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def verblijfadres(self) -> VerblijfadresBuitenland:
        """Gets the verblijfadres of this VerblijfplaatsBuitenlandVoorkomen.


        :return: The verblijfadres of this VerblijfplaatsBuitenlandVoorkomen.
        :rtype: VerblijfadresBuitenland
        """
        return self._verblijfadres

    @verblijfadres.setter
    def verblijfadres(self, verblijfadres: VerblijfadresBuitenland):
        """Sets the verblijfadres of this VerblijfplaatsBuitenlandVoorkomen.


        :param verblijfadres: The verblijfadres of this VerblijfplaatsBuitenlandVoorkomen.
        :type verblijfadres: VerblijfadresBuitenland
        """

        self._verblijfadres = verblijfadres

    @property
    def datum_van(self) -> AbstractDatum:
        """Gets the datum_van of this VerblijfplaatsBuitenlandVoorkomen.


        :return: The datum_van of this VerblijfplaatsBuitenlandVoorkomen.
        :rtype: AbstractDatum
        """
        return self._datum_van

    @datum_van.setter
    def datum_van(self, datum_van: AbstractDatum):
        """Sets the datum_van of this VerblijfplaatsBuitenlandVoorkomen.


        :param datum_van: The datum_van of this VerblijfplaatsBuitenlandVoorkomen.
        :type datum_van: AbstractDatum
        """

        self._datum_van = datum_van

    @property
    def datum_tot(self) -> AbstractDatum:
        """Gets the datum_tot of this VerblijfplaatsBuitenlandVoorkomen.


        :return: The datum_tot of this VerblijfplaatsBuitenlandVoorkomen.
        :rtype: AbstractDatum
        """
        return self._datum_tot

    @datum_tot.setter
    def datum_tot(self, datum_tot: AbstractDatum):
        """Sets the datum_tot of this VerblijfplaatsBuitenlandVoorkomen.


        :param datum_tot: The datum_tot of this VerblijfplaatsBuitenlandVoorkomen.
        :type datum_tot: AbstractDatum
        """

        self._datum_tot = datum_tot

    @property
    def gemeente_van_inschrijving(self) -> Waardetabel:
        """Gets the gemeente_van_inschrijving of this VerblijfplaatsBuitenlandVoorkomen.


        :return: The gemeente_van_inschrijving of this VerblijfplaatsBuitenlandVoorkomen.
        :rtype: Waardetabel
        """
        return self._gemeente_van_inschrijving

    @gemeente_van_inschrijving.setter
    def gemeente_van_inschrijving(self, gemeente_van_inschrijving: Waardetabel):
        """Sets the gemeente_van_inschrijving of this VerblijfplaatsBuitenlandVoorkomen.


        :param gemeente_van_inschrijving: The gemeente_van_inschrijving of this VerblijfplaatsBuitenlandVoorkomen.
        :type gemeente_van_inschrijving: Waardetabel
        """

        self._gemeente_van_inschrijving = gemeente_van_inschrijving

    @property
    def in_onderzoek(self) -> VerblijfplaatsBuitenlandVoorkomenInOnderzoek:
        """Gets the in_onderzoek of this VerblijfplaatsBuitenlandVoorkomen.


        :return: The in_onderzoek of this VerblijfplaatsBuitenlandVoorkomen.
        :rtype: VerblijfplaatsBuitenlandVoorkomenInOnderzoek
        """
        return self._in_onderzoek

    @in_onderzoek.setter
    def in_onderzoek(self, in_onderzoek: VerblijfplaatsBuitenlandVoorkomenInOnderzoek):
        """Sets the in_onderzoek of this VerblijfplaatsBuitenlandVoorkomen.


        :param in_onderzoek: The in_onderzoek of this VerblijfplaatsBuitenlandVoorkomen.
        :type in_onderzoek: VerblijfplaatsBuitenlandVoorkomenInOnderzoek
        """

        self._in_onderzoek = in_onderzoek

    @property
    def rni(self) -> RniDeelnemer:
        """Gets the rni of this VerblijfplaatsBuitenlandVoorkomen.


        :return: The rni of this VerblijfplaatsBuitenlandVoorkomen.
        :rtype: RniDeelnemer
        """
        return self._rni

    @rni.setter
    def rni(self, rni: RniDeelnemer):
        """Sets the rni of this VerblijfplaatsBuitenlandVoorkomen.


        :param rni: The rni of this VerblijfplaatsBuitenlandVoorkomen.
        :type rni: RniDeelnemer
        """

        self._rni = rni

    @property
    def adressering(self) -> AdresseringBuitenland:
        """Gets the adressering of this VerblijfplaatsBuitenlandVoorkomen.


        :return: The adressering of this VerblijfplaatsBuitenlandVoorkomen.
        :rtype: AdresseringBuitenland
        """
        return self._adressering

    @adressering.setter
    def adressering(self, adressering: AdresseringBuitenland):
        """Sets the adressering of this VerblijfplaatsBuitenlandVoorkomen.


        :param adressering: The adressering of this VerblijfplaatsBuitenlandVoorkomen.
        :type adressering: AdresseringBuitenland
        """

        self._adressering = adressering
