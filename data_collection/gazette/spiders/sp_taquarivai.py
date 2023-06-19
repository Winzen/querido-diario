from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrTaquarivaiSpider(DospGazetteSpider):
    TERRITORY_ID = "3553856"
    name = "sp_taquarivai"
    code = "5251"
    start_date = date(2019, 1, 24)
