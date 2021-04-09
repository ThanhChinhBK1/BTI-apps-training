import connexion
import six

from base.models.basic_response import BasicResponse  # noqa: E501
from base import util


def ping():  # noqa: E501
    """ping

    Test server health # noqa: E501


    :rtype: BasicResponse
    """
    return 'do some magic!'
