from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpSeteBarrasSpider(DospGazetteSpider):
    TERRITORY_ID = "3551801"
    name = "sp_sete_barras"
    code = "5228"
    start_date = date(2022, 11, 3)
