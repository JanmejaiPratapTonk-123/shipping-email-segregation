import re


def extract_tonnage(text):

    data = {
        "vessel_name": None,
        "account_name": None,
        "open_port": None,
        "open_date": None,
        "vessel_type": "Bulk Carrier",
        "vessel_size": None
    }

    text = text.upper()

    # Vessel Name
    vessel = re.search(r"MV\s+([A-Z\s]+)", text)

    if vessel:
        name = vessel.group(1)
        name = re.split(r"DWT|\(|OPEN|-|/", name)[0]
        data["vessel_name"] = name.strip()

    # Vessel Size
    size = re.search(r"/(\d+[K]?)\/", text)

    if not size:
        size = re.search(r"DWT\s*(\d+[K]?)", text)

    if not size:
        size = re.search(r"(\d+[K]?)\s*DWT", text)

    if size:
        data["vessel_size"] = size.group(1)

    open_match = re.search(
        r"OPEN\s+([0-9]{1,2}\s+[A-Z]+)\s+([A-Z\s,]+)",
        text
    )

    if open_match:
        data["open_date"] = open_match.group(1).strip()
        data["open_port"] = open_match.group(2).strip()

    on_match = re.search(
        r"OPEN\s+([A-Z\s]+)\s+ON\s+([0-9]{1,2}\s+[A-Z]+)",
        text
    )

    if on_match:
        data["open_port"] = on_match.group(1).strip()
        data["open_date"] = on_match.group(2).strip()

    oa_match = re.search(
        r"OPEN\s+([A-Z\s,]+)\s+O/A\s+([A-Z0-9\s]+)",
        text
    )

    if oa_match:
        data["open_port"] = oa_match.group(1).strip()
        data["open_date"] = oa_match.group(2).strip()

    if not data["open_port"]:

        alt = re.search(
            r"-\s*([A-Z\s]+)\s*,\s*([0-9A-Z\s]+(?:JUNE|JULY|MAY))",
            text
        )

        if alt:
            data["open_port"] = alt.group(1).strip()
            data["open_date"] = alt.group(2).strip()

    return data