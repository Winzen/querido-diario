from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpAmericoDeCamposSpider(DospGazetteSpider):
    TERRITORY_ID = "3501806"
    name = "sp_americo_de_campos"
    code = "4669"
    start_date = date(2014, 6, 25)
