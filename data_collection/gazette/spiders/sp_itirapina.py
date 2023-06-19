from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrItirapinaSpider(DospGazetteSpider):
    TERRITORY_ID = "3523602"
    name = "sp_itirapina"
    code = "4920"
    start_date = date(2019, 2, 13)
