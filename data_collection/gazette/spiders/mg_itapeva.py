from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrItapevaSpider(DospGazetteSpider):
    TERRITORY_ID = "3522406"
    name = "mg_itapeva"
    code = "4907"
    start_date = date(2017, 12, 18)
