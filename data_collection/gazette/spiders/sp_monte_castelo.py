from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpMonteCasteloSpider(DospGazetteSpider):
    TERRITORY_ID = "3531605"
    name = "sp_monte_castelo"
    code = "5004"
    start_date = date(2019, 5, 9)
