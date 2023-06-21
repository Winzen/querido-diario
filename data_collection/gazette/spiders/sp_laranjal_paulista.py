from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpLaranjalPaulistaSpider(DospGazetteSpider):
    TERRITORY_ID = "3526407"
    name = "sp_laranjal_paulista"
    code = "4949"
    start_date = date(2021, 3, 12)
