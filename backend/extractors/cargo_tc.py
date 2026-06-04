import re


def extract_tc(text):

    data = {
        "account_name": None,
        "cargo_name": None,
        "delivery_port": None,
        "redelivery_port": None,
        "duration": None,
        "laycan": None,
        "cargo_type": "Time Charter"
    }

    text = text.upper()

    delivery = re.search(
        r"DELIVERY PORT:\s*([A-Z ]+)",
        text
    )

    if delivery:
        data["delivery_port"] = delivery.group(1).strip()

    redelivery = re.search(
        r"REDELIVERY PORT:\s*([A-Z ]+)",
        text
    )

    if redelivery:
        data["redelivery_port"] = redelivery.group(1).strip()

    duration = re.search(
        r"DURATION:\s*([A-Z0-9 ]+)",
        text
    )

    if duration:
        data["duration"] = duration.group(1).strip()

    laycan = re.search(
        r"LAYCAN:\s*([A-Z0-9 ]+)",
        text
    )

    if laycan:
        data["laycan"] = laycan.group(1).strip()

    cargo = re.search(
        r"CARGO:\s*([A-Z0-9 ]+)",
        text
    )

    if cargo:
        data["cargo_name"] = cargo.group(1).strip()

    return data