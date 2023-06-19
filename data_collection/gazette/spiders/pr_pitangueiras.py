from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrPitangueirasSpider(DospGazetteSpider):
    TERRITORY_ID = "3539509"
    name = "pr_pitangueiras"
    code = "5092"
    start_date = date(2017, 9, 12)
