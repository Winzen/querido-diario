from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrRubineiaSpider(DospGazetteSpider):
    TERRITORY_ID = "3544509"
    name = "sp_rubineia"
    code = "5150"
    start_date = date(2019, 7, 2)
