from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrItarareSpider(DospGazetteSpider):
    TERRITORY_ID = "3523206"
    name = "sp_itarare"
    code = "4916"
    start_date = date(2018, 4, 6)
