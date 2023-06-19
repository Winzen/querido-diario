from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrRegenteFeijoSpider(DospGazetteSpider):
    TERRITORY_ID = "3542404"
    name = "sp_regente_feijo"
    code = "5126"
    start_date = date(2018, 10, 23)
