from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrMorroAgudoSpider(DospGazetteSpider):
    TERRITORY_ID = "3531902"
    name = "sp_morro_agudo"
    code = "5007"
    start_date = date(2017, 1, 24)
