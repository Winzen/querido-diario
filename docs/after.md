# Logicas De Spiders já estabelecidas
  Antes de começar a analise do site, vale a pena verificar se por a caso a logica dele já foi trabalhada em alguma das nossas classes prestabelecida.
  Elas são:
  - [Aplus](/data_collection/gazette/spiders/base/aplus.py)
  - [Doem](/data_collection/gazette/spiders/base/doem.py)
  - [Dosp](/data_collection/gazette/spiders/base/dosp.py)
  - [Fecam](/data_collection/gazette/spiders/base/fecam.py)
  - [Imprensa Oficial](/data_collection/gazette/spiders/base/imprensa_oficial.py)
  - [instar](/data_collection/gazette/spiders/base/instar.py)
  - [Sigpub](/data_collection/gazette/spiders/base/sigpub.py)

## Exemplo de como utilizar
Basicamente localizado uma classe que você pode estar utilizando.

Basta criar uma novo arquivo dentro de  

Exemplo Script completo ➡️ [Link](/data_collection/gazette/spiders/ba_acajutiba.py)
```python
class BaAcajutibaSpider(DoemGazetteSpider):
    TERRITORY_ID = "2900306"
    name = "ba_acajutiba"
    start_date = date(2018, 1, 2)
    state_city_url_part = "ba/acajutiba"
```
