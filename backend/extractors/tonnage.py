import re


def extract_tonnage(text):

    vessel_name = None
    vessel_size = None
    open_port = None
    open_date = None

    vessel_match = re.search(
        r'MV\s+([A-Z\s]+?)\s+DWT',
        text,
        re.IGNORECASE
    )

    if vessel_match:
        vessel_name = vessel_match.group(1).strip()

    size_match = re.search(
        r'DWT\s+(\d+)',
        text,
        re.IGNORECASE
    )

    if size_match:
        vessel_size = size_match.group(1)

    open_match = re.search(
        r'OPEN\s+([A-Z\s,]+)\s+O/A\s+([A-Z0-9\s\-]+)',
        text,
        re.IGNORECASE
    )

    if open_match:
        open_port = open_match.group(1).strip()
        open_date = open_match.group(2).strip()

    return {
        "vessel_name": vessel_name,
        "vessel_size": vessel_size,
        "open_port": open_port,
        "open_date": open_date
    }