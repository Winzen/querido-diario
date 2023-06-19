from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrMarabaPaulistaSpider(DospGazetteSpider):
    TERRITORY_ID = "3528700"
    name = "sp_maraba_paulista"
    code = "4973"
    start_date = date(2018, 12, 12)
