# Logicas de spiders já estabelecidas
  Antes de começar a analise do site, vale a pena verificar se por a caso a logica dele já foi trabalhada em alguma das nossas `class` preestabelecida.
  
  Elas são:
  - [Aplus](/data_collection/gazette/spiders/base/aplus.py)
  - [Doem](/data_collection/gazette/spiders/base/doem.py)
  - [Dosp](/data_collection/gazette/spiders/base/dosp.py)
  - [Fecam](/data_collection/gazette/spiders/base/fecam.py)
  - [Imprensa Oficial](/data_collection/gazette/spiders/base/imprensa_oficial.py)
  - [instar](/data_collection/gazette/spiders/base/instar.py)
  - [Sigpub](/data_collection/gazette/spiders/base/sigpub.py)

## Onde se encontra

```console
 /data_collection/gazette/spiders/base
```

## Exemplo de como utilizar
Basicamente localizado uma `class` que você pode estar utilizando na sua spider.

Basta criar uma novo arquivo dentro de:

```console
/data_collection/gazette/spiders
```
Import a `class` selecionada para o arquivo spider que esta trabalhando. Normalmente import `date` de `datetime` para preencher `start_date`

```python
from gazette.spiders.base.doem import DoemGazetteSpider
from datetime import date
```

Crie uma nova `class` com a class preestabelecida selecionada como herança.

```python
class BaAcajutibaSpider(DoemGazetteSpider):
    TERRITORY_ID = "2900306"
    name = "ba_acajutiba"
    start_date = date(2018, 1, 2)
    state_city_url_part = "ba/acajutiba"
```
Exemplo Script completo ➡️ [Link](/data_collection/gazette/spiders/ba_acajutiba.py)

# Tempo de coleta

Cuidado com o tempo que as vezes o spider leva para realizar toda a operação. As vezes é necessario notificar isso no seu PR, para uma mudança no disparador de rotina dessa spider.
**O tempo limite de coleta é de 1 hora**

# Spiders com mais de um site de coleta.

Bom verificar se todos os diarios estão disponiveis em um ou mais sites. Caso esteja em mais de um site, tome a abordagem que se encontra aqui ➡️ [849](https://github.com/okfn-brasil/querido-diario/pull/849)
