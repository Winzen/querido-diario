from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpCapelaDoAltoSpider(DospGazetteSpider):
    TERRITORY_ID = "3510302"
    name = "sp_capela_do_alto"
    code = "4767"
    start_date = date(2018, 9, 28)
