from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrMirassolSpider(DospGazetteSpider):
    TERRITORY_ID = "3530300"
    name = "sp_mirassol"
    code = "4991"
    start_date = date(2018, 3, 5)
