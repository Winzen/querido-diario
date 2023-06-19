from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrAgudosSpider(DospGazetteSpider):
    TERRITORY_ID = "3500709"
    name = "sp_agudos"
    code = "4656"
    start_date = date(2017, 6, 27)
