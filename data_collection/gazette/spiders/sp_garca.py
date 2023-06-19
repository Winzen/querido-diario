from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrGarcaSpider(DospGazetteSpider):
    TERRITORY_ID = "3516705"
    name = "sp_garca"
    code = "4841"
    start_date = date(2014, 8, 25)
