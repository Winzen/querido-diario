from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrParaisoSpider(DospGazetteSpider):
    TERRITORY_ID = "4212239"
    name = "sp_paraiso"
    code = "5052"
    start_date = date(2015, 9, 28)
