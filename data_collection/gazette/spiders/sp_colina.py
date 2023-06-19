from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrColinaSpider(DospGazetteSpider):
    TERRITORY_ID = "3512001"
    name = "sp_colina"
    code = "4784"
    start_date = date(2022, 4, 19)
