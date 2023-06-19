from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrFernandoPrestesSpider(DospGazetteSpider):
    TERRITORY_ID = "3515608"
    name = "sp_fernando_prestes"
    code = "4828"
    start_date = date(2013, 10, 22)
