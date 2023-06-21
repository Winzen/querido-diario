from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpSantoExpeditoSpider(DospGazetteSpider):
    TERRITORY_ID = "3548302"
    name = "sp_santo_expedito"
    code = "5191"
    start_date = date(2020, 4, 29)
