==========================================================
python-iso3166 - Standalone ISO 3166-1 country definitions
==========================================================

:Authors:
        Mike Spindel
:Version: 0.5.1


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

or if you would like to use a table of other common names for lookup:
::
  >>> from iso3166 import approx_countries as countries
  >>>
  >>> countries["Ivory Coast"]
      Country(name=u"C\xf4te d'Ivoire", alpha2='CI', alpha3='CIV', numeric='384')
  >>> countries[u"Côte d'Ivoire"]
      Country(name=u"C\xf4te d'Ivoire", alpha2='CI', alpha3='CIV', numeric='384')

get local display name of a country
::
  >>> from iso3166 import countries
  >>>
  >>> us = countries.get('us')
  >>> print us.local_name('zh_TW')
  美國
  >>> print us.local_name('ja_JP')
  アメリカ合衆国
