from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpGuarantaSpider(DospGazetteSpider):
    TERRITORY_ID = "3518107"
    name = "sp_guaranta"
    code = "4856"
    start_date = date(2017, 1, 23)
