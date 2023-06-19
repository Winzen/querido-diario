from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrSantaMercedesSpider(DospGazetteSpider):
    TERRITORY_ID = "3547106"
    name = "sp_santa_mercedes"
    code = "5177"
    start_date = date(2019, 3, 1)
