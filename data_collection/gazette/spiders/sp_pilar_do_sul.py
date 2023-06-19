from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrPilarDoSulSpider(DospGazetteSpider):
    TERRITORY_ID = "3537909"
    name = "sp_pilar_do_sul"
    code = "5077"
    start_date = date(2022, 7, 1)
