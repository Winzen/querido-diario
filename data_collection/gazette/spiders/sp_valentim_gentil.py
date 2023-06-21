from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpValentimGentilSpider(DospGazetteSpider):
    TERRITORY_ID = "3556107"
    name = "sp_valentim_gentil"
    code = "5279"
    start_date = date(2015, 11, 5)
