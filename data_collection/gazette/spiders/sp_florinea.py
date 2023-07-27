from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpFlorineaSpider(DospGazetteSpider):
    TERRITORY_ID = "None"
    name = "sp_florinea"
    code = "4834"
    start_date = date(2017, 10, 26)
