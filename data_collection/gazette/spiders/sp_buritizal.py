from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrBuritizalSpider(DospGazetteSpider):
    TERRITORY_ID = "3508207"
    name = "sp_buritizal"
    code = "4742"
    start_date = date(2022, 10, 26)
