from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpAlvaroDeCarvalhoSpider(DospGazetteSpider):
    TERRITORY_ID = "3501400"
    name = "sp_alvaro_de_carvalho"
    code = "4665"
    start_date = date(2018, 4, 4)
