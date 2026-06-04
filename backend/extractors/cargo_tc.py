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

    # Delivery Port
    delivery = re.search(
        r"DELIVERY PORT[:\s]+([A-Z\s]+?)(?:\n|$)",
        text
    )

    if delivery:
        data["delivery_port"] = delivery.group(1).strip()

    # Redelivery Port
    redelivery = re.search(
        r"REDELIVERY PORT[:\s]+([A-Z\s]+?)(?:\n|$)",
        text
    )

    if redelivery:
        data["redelivery_port"] = redelivery.group(1).strip()

    # Duration
    duration = re.search(
        r"DURATION[:\s]+([0-9A-Z\s]+?)(?:\n|$)",
        text
    )

    if duration:
        data["duration"] = duration.group(1).strip()

    # Laycan
    laycan = re.search(
        r"LAYCAN[:\s]+([0-9A-Z\s]+?)(?:\n|$)",
        text
    )

    if laycan:
        data["laycan"] = laycan.group(1).strip()

    # Cargo
    cargo = re.search(
        r"CARGO[:\s]+([A-Z\s]+?)(?:\n|$)",
        text
    )

    if cargo:
        data["cargo_name"] = cargo.group(1).strip()

    return data