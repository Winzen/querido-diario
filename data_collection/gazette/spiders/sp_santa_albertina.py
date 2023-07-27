from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpSantaAlbertinaSpider(DospGazetteSpider):
    TERRITORY_ID = "3545704"
    name = "sp_santa_albertina"
    code = "5163"
    start_date = date(2021, 10, 8)
