from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpPresidenteVenceslauSpider(DospGazetteSpider):
    TERRITORY_ID = "3541505"
    name = "sp_presidente_venceslau"
    code = "5116"
    start_date = date(2021, 3, 4)
