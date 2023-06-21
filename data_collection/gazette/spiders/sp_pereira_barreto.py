from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpPereiraBarretoSpider(DospGazetteSpider):
    TERRITORY_ID = "3537404"
    name = "sp_pereira_barreto"
    code = "5072"
    start_date = date(2014, 3, 29)
