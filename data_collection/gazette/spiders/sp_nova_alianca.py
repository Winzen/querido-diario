from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrNovaAliancaSpider(DospGazetteSpider):
    TERRITORY_ID = "3532801"
    name = "sp_nova_alianca"
    code = "5018"
    start_date = date(2021, 1, 29)
