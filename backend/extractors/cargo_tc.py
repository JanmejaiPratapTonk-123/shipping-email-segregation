import re


def extract_tc(text):

    delivery = None
    redelivery = None
    duration = None

    delivery_match = re.search(
        r'DELIVERY\s+([A-Z\s]+)',
        text,
        re.IGNORECASE
    )

    if delivery_match:
        delivery = delivery_match.group(1).strip()

    redelivery_match = re.search(
        r'REDELIVERY\s+([A-Z\s]+)',
        text,
        re.IGNORECASE
    )

    if redelivery_match:
        redelivery = redelivery_match.group(1).strip()

    duration_match = re.search(
        r'DURATION\s+ABT\s+([A-Z0-9\s\-]+)',
        text,
        re.IGNORECASE
    )

    if duration_match:
        duration = duration_match.group(1).strip()

    return {
        "delivery_port": delivery,
        "redelivery_port": redelivery,
        "duration": duration
    }