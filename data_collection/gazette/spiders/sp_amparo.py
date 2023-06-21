from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpAmparoSpider(DospGazetteSpider):
    TERRITORY_ID = "3501905"
    name = "sp_amparo"
    code = "4670"
    start_date = date(2019, 10, 18)
