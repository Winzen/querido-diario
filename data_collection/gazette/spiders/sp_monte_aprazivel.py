from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpMonteAprazivelSpider(DospGazetteSpider):
    TERRITORY_ID = "3531407"
    name = "sp_monte_aprazivel"
    code = "5002"
    start_date = date(2017, 5, 2)
