from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrMaracaiSpider(DospGazetteSpider):
    TERRITORY_ID = "3528809"
    name = "sp_maracai"
    code = "4974"
    start_date = date(2017, 8, 8)
