==========================================================
python-iso3166 - Standalone ISO 3166-1 country definitions
==========================================================

:Authors:
        Mike Spindel
:Version: 0.2


ISO 3166-1 defines two-letter, three-letter, and three-digit country
codes.  `python-iso3166` is a self-contained module that converts
between these codes and the corresponding country name.


Installation
============

::

  $ pip install iso3166


Usage
=====

::

  >>> from iso3166 import countries
  >>>
  >>> countries.get('us')
  Country(name=u'United States', alpha2='US', alpha3='USA', numeric='840')
  >>> countries.get('ala')
  Country(name=u'\xc5land Islands', alpha2='AX', alpha3='ALA', numeric='248')
  >>> countries.get(8)
  Country(name=u'Albania', alpha2='AL', alpha3='ALB', numeric='008')
