import datetime
import json

from urllib.request import ssl, socket


def check_ssl(hostname: str, port: str) -> dict:
    """
    This function is check ssl certificate
    :param hostname:
    :param port:
    :return:
    """
    context = ssl.create_default_context()

    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            certificate = ssock.getpeercert()

    certExpires = datetime.datetime.strptime(
        certificate['notAfter'], '%b %d %H:%M:%S %Y %Z')

    return {
        'Expiration Day': f"{certExpires.year}-{certExpires.month}-{certExpires.day}",
        'Remaining Day': (certExpires - datetime.datetime.now()).days
    }


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
