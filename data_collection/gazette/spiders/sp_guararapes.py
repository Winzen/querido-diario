from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrGuararapesSpider(DospGazetteSpider):
    TERRITORY_ID = "3518206"
    name = "sp_guararapes"
    code = "4857"
    start_date = date(2016, 10, 20)
