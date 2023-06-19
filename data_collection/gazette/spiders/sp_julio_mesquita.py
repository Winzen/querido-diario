from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrJulioMesquitaSpider(DospGazetteSpider):
    TERRITORY_ID = "3525805"
    name = "sp_julio_mesquita"
    code = "4942"
    start_date = date(2018, 3, 12)
