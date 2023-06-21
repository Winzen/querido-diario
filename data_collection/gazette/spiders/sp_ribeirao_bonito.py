from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpRibeiraoBonitoSpider(DospGazetteSpider):
    TERRITORY_ID = "3542909"
    name = "sp_ribeirao_bonito"
    code = "5131"
    start_date = date(2016, 6, 21)
