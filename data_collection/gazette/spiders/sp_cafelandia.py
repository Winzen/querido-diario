from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpCafelandiaSpider(DospGazetteSpider):
    TERRITORY_ID = "3508801"
    name = "sp_cafelandia"
    code = "4748"
    start_date = date(2017, 6, 12)
