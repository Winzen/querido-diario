from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpIacangaSpider(DospGazetteSpider):
    TERRITORY_ID = "3519105"
    name = "sp_iacanga"
    code = "4869"
    start_date = date(2017, 4, 24)
