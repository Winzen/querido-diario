from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpCastilhoSpider(DospGazetteSpider):
    TERRITORY_ID = "3511003"
    name = "sp_castilho"
    code = "4774"
    start_date = date(2018, 7, 18)
