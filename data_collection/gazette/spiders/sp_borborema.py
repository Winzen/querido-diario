from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpBorboremaSpider(DospGazetteSpider):
    TERRITORY_ID = "3507407"
    name = "sp_borborema"
    code = "4732"
    start_date = date(2016, 5, 3)
