from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpMonteiroLobatoSpider(DospGazetteSpider):
    TERRITORY_ID = "3531704"
    name = "sp_monteiro_lobato"
    code = "5006"
    start_date = date(2020, 11, 26)
