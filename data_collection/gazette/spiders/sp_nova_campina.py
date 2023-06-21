from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpNovaCampinaSpider(DospGazetteSpider):
    TERRITORY_ID = "3532827"
    name = "sp_nova_campina"
    code = "5019"
    start_date = date(2021, 2, 4)
