from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpSantoAnastacioSpider(DospGazetteSpider):
    TERRITORY_ID = "3547700"
    name = "sp_santo_anastacio"
    code = "5184"
    start_date = date(2020, 9, 23)
