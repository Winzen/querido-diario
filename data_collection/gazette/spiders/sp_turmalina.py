from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrTurmalinaSpider(DospGazetteSpider):
    TERRITORY_ID = "3169703"
    name = "sp_turmalina"
    code = "5270"
    start_date = date(2017, 12, 18)
