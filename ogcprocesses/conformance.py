from ogcprocesses.utils.urls import url
from ogcprocesses.utils.helper import get_data
conformance_url = url().conformance_urls()

def metadata(f="json") -> dict:
    print(conformance_url["conformance_url"])
    data = get_data(conformance_url["conformance_url"],f)
    return data