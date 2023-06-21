from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpTeodoroSampaioSpider(DospGazetteSpider):
    TERRITORY_ID = "3554300"
    name = "sp_teodoro_sampaio"
    code = "5257"
    start_date = date(2018, 8, 28)
