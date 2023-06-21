from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpJoseBonifacioSpider(DospGazetteSpider):
    TERRITORY_ID = "3525706"
    name = "sp_jose_bonifacio"
    code = "4941"
    start_date = date(2014, 9, 30)
