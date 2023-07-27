from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpSantaSaleteSpider(DospGazetteSpider):
    TERRITORY_ID = "3547650"
    name = "sp_santa_salete"
    code = "5181"
    start_date = date(2023, 3, 31)
