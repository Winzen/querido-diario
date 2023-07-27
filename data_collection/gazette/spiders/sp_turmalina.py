from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpTurmalinaSpider(DospGazetteSpider):
    TERRITORY_ID = "3555307"
    name = "sp_turmalina"
    code = "5270"
    start_date = date(2017, 12, 18)
