Web [pyworking.cz](https://pyworking.cz/)
=========================================

[![Build Status](https://travis-ci.org/pyvec/pyworking.cz.svg?branch=master)](https://travis-ci.org/pyvec/pyworking.cz)


Jak to rozběhat u sebe
----------------------

O vše se umí postarat Makefile - mělo by stačit napsat `make flask-run` a automaticky se vytvoří Python venv, nainstalují do něj závislosti a spustí se webovka v development režimu (Flask).

Testy se spustí pomocí `make check`

Poznámka: pokud si projekt nainstalujete přes pip bez parametru `-e`, budete muset nastavit env proměnnou DATA_DIR (viz [#15](https://github.com/pyvec/pyworking.cz/issues/15)).


Jak to nasadit
--------------

Zatím nasazuje ručně [Petr M.](https://github.com/messa) :innocent:
