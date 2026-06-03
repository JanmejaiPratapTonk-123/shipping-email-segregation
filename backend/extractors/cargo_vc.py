import re


def extract_vc(text):

    loading_port = None
    discharge_port = None
    laycan = None

    lp_match = re.search(
        r'LOAD PORT\s*:?\s*([A-Z\s,]+)',
        text,
        re.IGNORECASE
    )

    if lp_match:
        loading_port = lp_match.group(1).strip()

    dp_match = re.search(
        r'DISCHARGE PORT\s*:?\s*([A-Z\s,+]+)',
        text,
        re.IGNORECASE
    )

    if dp_match:
        discharge_port = dp_match.group(1).strip()

    laycan_match = re.search(
        r'LAYCAN\s*:?\s*([A-Z0-9\s\-]+)',
        text,
        re.IGNORECASE
    )

    if laycan_match:
        laycan = laycan_match.group(1).strip()

    return {
        "loading_port": loading_port,
        "discharge_port": discharge_port,
        "laycan": laycan
    }