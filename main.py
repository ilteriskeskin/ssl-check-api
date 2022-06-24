import datetime
import logging
import json

from urllib.request import ssl, socket


logger = logging.getLogger(__name__)


def check_ssl(hostname: str, port: str) -> dict:
    """
    This function is check ssl certificate
    :param hostname:
    :param port:
    :return:
    """
    context = ssl.create_default_context()

    try:
        with socket.create_connection(address=(hostname, port), timeout=3) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                certificate = ssock.getpeercert()

        certExpires = datetime.datetime.strptime(
            certificate['notAfter'], '%b %d %H:%M:%S %Y %Z')

        data = {
            'status': 200,
            'expiration_day': f"{certExpires.year}-{certExpires.month}-{certExpires.day}",
            'remaining_day': (certExpires - datetime.datetime.now()).days
        }
    except Exception as e:
        logger.error(e)
        data = {
            'status': 500,
            'message': 'Server Error! Try again or contact admin.'
        }

    return data


def run(event, context) -> list:
    """
    Check SSL Service
    :param event:
    :param context:
    :return:
    """
    request_body = json.loads(event['body'])
    hostname = request_body.get('hostname')
    port = request_body.get('port', 443)

    if not hostname:
        return {'ok': False, 'message': 'Wrong request parameters.'}

    return check_ssl(hostname=hostname, port=str(port))
