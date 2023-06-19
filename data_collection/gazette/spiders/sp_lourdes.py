from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrLourdesSpider(DospGazetteSpider):
    TERRITORY_ID = "3527256"
    name = "sp_lourdes"
    code = "4958"
    start_date = date(2017, 9, 28)
