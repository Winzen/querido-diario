from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpLindoiaSpider(DospGazetteSpider):
    TERRITORY_ID = "3527009"
    name = "sp_lindoia"
    code = "4955"
    start_date = date(2020, 1, 28)
