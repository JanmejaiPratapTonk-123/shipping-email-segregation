import re


def extract_vc(text):

    data = {
        "account_name": None,
        "cargo_name": None,
        "loading_port": None,
        "discharge_port": None,
        "laycan": None,
        "cargo_type": "Voyage Charter"
    }

    text = text.upper()

    cargo = re.search(
        r"CARGO[:\s]*([0-9,\sA-Z]+(?:UREA|COAL|SLAG|CLINKER))",
        text
    )

    if not cargo:
        cargo = re.search(
            r"([0-9,\sA-Z]+(?:UREA|COAL|SLAG|CLINKER))",
            text
        )

    if cargo:
        data["cargo_name"] = cargo.group(1).strip()

    lp = re.search(
        r"(LOAD PORT|POL|LP)[:\s]+([A-Z\s]+?)(DISCHARGE PORT|POD|DP)",
        text
    )

    if lp:
        data["loading_port"] = lp.group(2).strip()

    dp = re.search(
        r"(DISCHARGE PORT|POD|DP)[:\s]+([A-Z\s]+?)(LAYCAN|$)",
        text
    )

    if dp:
        data["discharge_port"] = dp.group(2).strip()

    laycan = re.search(
        r"LAYCAN[:\s]+([0-9A-Z\-\s]+)",
        text
    )

    if laycan:
        data["laycan"] = laycan.group(1).strip()

    return data