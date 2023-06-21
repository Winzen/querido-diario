from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class MgItapevaSpider(DospGazetteSpider):
    TERRITORY_ID = "3133600"
    name = "mg_itapeva"
    code = "4907"
    start_date = date(2017, 12, 18)
