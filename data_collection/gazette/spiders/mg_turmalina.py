from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class MgTurmalinaSpider(DospGazetteSpider):
    TERRITORY_ID = "3169703"
    name = "mg_turmalina"
    code = "5270"
    start_date = date(2017, 12, 18)
