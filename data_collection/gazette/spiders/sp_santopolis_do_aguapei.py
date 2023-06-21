from datetime import date

from gazette.spiders.base.dosp import DospGazetteSpider


class SpSantopolisDoAguapeiSpider(DospGazetteSpider):
    TERRITORY_ID = "3548401"
    name = "sp_santopolis_do_aguapei"
    code = "5192"
    start_date = date(2014, 7, 1)
