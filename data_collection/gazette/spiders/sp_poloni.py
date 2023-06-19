from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrPoloniSpider(DospGazetteSpider):
    TERRITORY_ID = "3539905"
    name = "sp_poloni"
    code = "5096"
    start_date = date(2020, 1, 13)
