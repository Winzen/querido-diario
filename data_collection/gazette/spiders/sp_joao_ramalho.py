from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpJoaoRamalhoSpider(DospGazetteSpider):
    TERRITORY_ID = "3525607"
    name = "sp_joao_ramalho"
    code = "4940"
    start_date = date(2020, 3, 24)
