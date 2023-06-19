from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrAguasDeLindoiaSpider(DospGazetteSpider):
    TERRITORY_ID = "3500501"
    name = "sp_aguas_de_lindoia"
    code = "4653"
    start_date = date(2020, 1, 31)
