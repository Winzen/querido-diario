from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrJaborandiSpider(DospGazetteSpider):
    TERRITORY_ID = "2917359"
    name = "sp_jaborandi"
    code = "4926"
    start_date = date(2017, 9, 20)
