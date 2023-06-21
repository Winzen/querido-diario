from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpTaquaritingaSpider(DospGazetteSpider):
    TERRITORY_ID = "3553708"
    name = "sp_taquaritinga"
    code = "5249"
    start_date = date(2016, 1, 8)
