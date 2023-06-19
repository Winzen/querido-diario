from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrNovaIndependenciaSpider(DospGazetteSpider):
    TERRITORY_ID = "3533205"
    name = "sp_nova_independencia"
    code = "5025"
    start_date = date(2021, 7, 13)
