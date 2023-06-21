from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpBocainaSpider(DospGazetteSpider):
    TERRITORY_ID = "3506805"
    name = "sp_bocaina"
    code = "4725"
    start_date = date(2018, 7, 23)
