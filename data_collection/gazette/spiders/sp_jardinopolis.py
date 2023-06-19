from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrJardinopolisSpider(DospGazetteSpider):
    TERRITORY_ID = "3525102"
    name = "sp_jardinopolis"
    code = "4935"
    start_date = date(2020, 3, 11)
