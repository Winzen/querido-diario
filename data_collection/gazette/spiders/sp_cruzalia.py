from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrCruzaliaSpider(DospGazetteSpider):
    TERRITORY_ID = "3513306"
    name = "sp_cruzalia"
    code = "4797"
    start_date = date(2019, 3, 14)
