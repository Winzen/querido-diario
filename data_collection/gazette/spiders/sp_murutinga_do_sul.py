from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrMurutingaDoSulSpider(DospGazetteSpider):
    TERRITORY_ID = "3532108"
    name = "sp_murutinga_do_sul"
    code = "5010"
    start_date = date(2018, 7, 26)
