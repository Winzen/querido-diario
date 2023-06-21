from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpGabrielMonteiroSpider(DospGazetteSpider):
    TERRITORY_ID = "3516507"
    name = "sp_gabriel_monteiro"
    code = "4839"
    start_date = date(2018, 8, 15)
