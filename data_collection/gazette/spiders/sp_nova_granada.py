from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpNovaGranadaSpider(DospGazetteSpider):
    TERRITORY_ID = "3533007"
    name = "sp_nova_granada"
    code = "5023"
    start_date = date(2018, 2, 16)
