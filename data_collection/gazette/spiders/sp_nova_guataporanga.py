from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpNovaGuataporangaSpider(DospGazetteSpider):
    TERRITORY_ID = "3533106"
    name = "sp_nova_guataporanga"
    code = "5024"
    start_date = date(2019, 9, 12)
