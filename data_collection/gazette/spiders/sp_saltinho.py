from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrSaltinhoSpider(DospGazetteSpider):
    TERRITORY_ID = "3545159"
    name = "sp_saltinho"
    code = "5157"
    start_date = date(2019, 6, 5)
