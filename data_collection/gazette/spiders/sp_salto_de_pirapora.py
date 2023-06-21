from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpSaltoDePiraporaSpider(DospGazetteSpider):
    TERRITORY_ID = "3545308"
    name = "sp_salto_de_pirapora"
    code = "5159"
    start_date = date(2021, 1, 5)
