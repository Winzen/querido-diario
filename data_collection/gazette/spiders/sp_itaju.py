from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpItajuSpider(DospGazetteSpider):
    TERRITORY_ID = "3522000"
    name = "sp_itaju"
    code = "4902"
    start_date = date(2018, 5, 25)
