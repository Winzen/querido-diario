from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpCardosoSpider(DospGazetteSpider):
    TERRITORY_ID = "3510708"
    name = "sp_cardoso"
    code = "4771"
    start_date = date(2019, 5, 8)
