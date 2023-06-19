from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrVitoriaBrasilSpider(DospGazetteSpider):
    TERRITORY_ID = "3556958"
    name = "sp_vitoria_brasil"
    code = "5290"
    start_date = date(2019, 2, 19)
