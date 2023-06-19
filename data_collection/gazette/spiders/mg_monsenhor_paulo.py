from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrMonsenhorPauloSpider(DospGazetteSpider):
    TERRITORY_ID = "3142601"
    name = "mg_monsenhor_paulo"
    code = "2032"
    start_date = date(2017, 4, 12)
