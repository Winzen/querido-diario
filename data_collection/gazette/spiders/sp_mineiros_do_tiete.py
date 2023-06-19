from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrMineirosDoTieteSpider(DospGazetteSpider):
    TERRITORY_ID = "3529807"
    name = "sp_mineiros_do_tiete"
    code = "4986"
    start_date = date(2018, 1, 10)
