from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpBentoDeAbreuSpider(DospGazetteSpider):
    TERRITORY_ID = "3506201"
    name = "sp_bento_de_abreu"
    code = "4718"
    start_date = date(2016, 6, 14)
