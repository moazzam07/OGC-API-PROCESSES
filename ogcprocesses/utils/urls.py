class url:
    def __init__(self):
        self.base_url = " http://www.opengis.net/def/rel/ogc/1.0/"
        self.conformance = "conformance"

    def landing_urls(self) -> dict:
        return {"landing_url": self.base_url}
    
    def conformance_urls(self) -> dict:
        return {"conformance_url": self.base_url + self.conformance}
