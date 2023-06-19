from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class PrCafezalDoSulSpider(DospGazetteSpider):
    TERRITORY_ID = "4103479"
    name = "pr_cafezal_do_sul"
    code = "2808"
    start_date = date(2016, 4, 14)
