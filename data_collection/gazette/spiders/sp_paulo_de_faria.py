from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpPauloDeFariaSpider(DospGazetteSpider):
    TERRITORY_ID = "3536604"
    name = "sp_paulo_de_faria"
    code = "5063"
    start_date = date(2018, 4, 26)
