from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrSantoAntonioDePosseSpider(DospGazetteSpider):
    TERRITORY_ID = "3548005"
    name = "sp_santo_antonio_de_posse"
    code = "5187"
    start_date = date(2018, 8, 10)
