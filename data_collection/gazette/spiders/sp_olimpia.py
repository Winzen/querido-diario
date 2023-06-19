from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrOlimpiaSpider(DospGazetteSpider):
    TERRITORY_ID = "3533908"
    name = "sp_olimpia"
    code = "5033"
    start_date = date(2017, 6, 27)
