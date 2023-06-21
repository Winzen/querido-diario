from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpJauSpider(DospGazetteSpider):
    TERRITORY_ID = "3525300"
    name = "sp_jau"
    code = "4937"
    start_date = date(2023, 1, 6)
