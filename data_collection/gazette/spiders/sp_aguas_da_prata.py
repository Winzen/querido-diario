from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrAguasDaPrataSpider(DospGazetteSpider):
    TERRITORY_ID = "3500402"
    name = "sp_aguas_da_prata"
    code = "4652"
    start_date = date(2018, 8, 23)
