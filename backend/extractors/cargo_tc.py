import re


def extract_tc(text):

    account_name = None
    cargo_name = None
    delivery = None
    redelivery = None
    duration = None
    laycan = None
    cargo_type = "Time Charter"

    delivery_match = re.search(
        r'DELIVERY\s+([A-Z\s]+?)\s+REDELIVERY',
        text,
        re.IGNORECASE
    )

    if delivery_match:
        delivery = delivery_match.group(1).strip()

    redelivery_match = re.search(
        r'REDELIVERY\s+([A-Z\s]+?)\s+DURATION',
        text,
        re.IGNORECASE
    )

    if redelivery_match:
        redelivery = redelivery_match.group(1).strip()

    duration_match = re.search(
        r'DURATION\s+ABT\s+([0-9\sA-Z]+?)\s+LAYCAN',
        text,
        re.IGNORECASE
    )

    if duration_match:
        duration = duration_match.group(1).strip()

    laycan_match = re.search(
        r'LAYCAN\s+([A-Z0-9\s]+?)\s+WITH',
        text,
        re.IGNORECASE
    )

    if laycan_match:
        laycan = laycan_match.group(1).strip()

    cargo_match = re.search(
        r'WITH\s+([A-Z\s]+)',
        text,
        re.IGNORECASE
    )

    if cargo_match:
        cargo_name = cargo_match.group(1).strip()

    return {
        "account_name": account_name,
        "cargo_name": cargo_name,
        "delivery_port": delivery,
        "redelivery_port": redelivery,
        "duration": duration,
        "laycan": laycan,
        "cargo_type": cargo_type
    }