Web [pyworking.cz](https://pyworking.cz/)
=========================================

[![Build Status](https://travis-ci.org/pyvec/pyworking.cz.svg?branch=master)](https://travis-ci.org/pyvec/pyworking.cz)


Jak to rozběhat u sebe
----------------------

O vše se umí postarat Makefile - mělo by stačit napsat `make flask-run` a automaticky se vytvoří Python venv, nainstalují do něj závislosti a spustí se webovka v development režimu (Flask).

Testy se spustí pomocí `make check`

V produkci web běží na Github Pages jako statická stránka generovaná pomocí Flask-Frozen, k tomu slouží target `make freeze`. Nasazení probíhá automaticky přes Github Actions do větve [gh-pages](https://github.com/pyvec/pyworking.cz/tree/gh-pages).

Poznámka: pokud si projekt nainstalujete přes pip bez parametru `-e`, budete muset nastavit env proměnnou DATA_DIR (viz [#15](https://github.com/pyvec/pyworking.cz/issues/15)).
