from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrVargemSpider(DospGazetteSpider):
    TERRITORY_ID = "4219150"
    name = "sp_vargem"
    code = "5282"
    start_date = date(2020, 2, 7)
