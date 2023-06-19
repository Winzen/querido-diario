from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrPalmaresPaulistaSpider(DospGazetteSpider):
    TERRITORY_ID = "3535101"
    name = "sp_palmares_paulista"
    code = "5046"
    start_date = date(2022, 3, 25)
