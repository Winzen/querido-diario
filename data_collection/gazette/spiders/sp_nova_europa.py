from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrNovaEuropaSpider(DospGazetteSpider):
    TERRITORY_ID = "3532900"
    name = "sp_nova_europa"
    code = "5022"
    start_date = date(2019, 1, 8)
