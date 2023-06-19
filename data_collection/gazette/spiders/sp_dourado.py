from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrDouradoSpider(DospGazetteSpider):
    TERRITORY_ID = "3514304"
    name = "sp_dourado"
    code = "4808"
    start_date = date(2017, 10, 17)
