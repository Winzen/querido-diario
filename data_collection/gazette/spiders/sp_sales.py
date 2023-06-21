from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpSalesSpider(DospGazetteSpider):
    TERRITORY_ID = "3544806"
    name = "sp_sales"
    code = "5153"
    start_date = date(2017, 12, 20)
