from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrBarraBonitaSpider(DospGazetteSpider):
    TERRITORY_ID = "3505302"
    name = "sp_barra_bonita"
    code = "4708"
    start_date = date(2021, 5, 18)
