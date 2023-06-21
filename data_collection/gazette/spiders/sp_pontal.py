from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpPontalSpider(DospGazetteSpider):
    TERRITORY_ID = "3540200"
    name = "sp_pontal"
    code = "5099"
    start_date = date(2022, 12, 29)
