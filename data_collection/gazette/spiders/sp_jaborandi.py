from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpJaborandiSpider(DospGazetteSpider):
    TERRITORY_ID = "3524204"
    name = "sp_jaborandi"
    code = "4926"
    start_date = date(2017, 9, 20)
