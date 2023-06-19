from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrAlvaresFlorenceSpider(DospGazetteSpider):
    TERRITORY_ID = "3501202"
    name = "sp_alvares_florence"
    code = "4663"
    start_date = date(2013, 3, 13)
