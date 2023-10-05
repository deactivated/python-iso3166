============================================================
 python-iso3166 - Standalone ISO 3166-1 country definitions
============================================================

:Authors:
        Mike Spindel
:Version: 2.1.1


ISO 3166-1 defines two-letter, three-letter, and three-digit country
codes.  `python-iso3166` is a self-contained module that converts
between these codes and the corresponding country name.


Installation
============

::

  $ pip install iso3166


Usage
=====

Country details
---------------

::

  >>> from iso3166 import countries
  >>>
  >>> countries.get('us')
  Country(name='United States of America', alpha2='US', alpha3='USA', numeric='840', apolitical_name='United States of America', flag='🇺🇸')
  >>> countries.get('ala')
  Country(name='Åland Islands', alpha2='AX', alpha3='ALA', numeric='248', apolitical_name='Åland Islands', flag='🇦🇽')
  >>> countries.get(8)
  Country(name='Albania', alpha2='AL', alpha3='ALB', numeric='008', apolitical_name='Albania', flag='🇦🇱'


Country lists and indexes
-------------------------

::

  >>> from iso3166 import countries

  >>> for c in countries:
         print(c)
  >>> Country(name='Afghanistan', alpha2='AF', alpha3='AFG', numeric='004', apolitical_name='Afghanistan', flag='🇦🇫')
  Country(name='Åland Islands', alpha2='AX', alpha3='ALA', numeric='248', apolitical_name='Åland Islands', flag='🇦🇽')
  Country(name='Albania', alpha2='AL', alpha3='ALB', numeric='008', apolitical_name='Albania', flag='🇦🇱')
  Country(name='Algeria', alpha2='DZ', alpha3='DZA', numeric='012', apolitical_name='Algeria', flag='🇩🇿')

::

  >>> import iso3166

  >>> iso3166.countries_by_name
  >>> {'AFGHANISTAN': Country(name='Afghanistan', alpha2='AF', alpha3='AFG', numeric='004', apolitical_name='Afghanistan', flag='🇦🇫'),
  'ÅLAND ISLANDS': Country(name='Åland Islands', alpha2='AX', alpha3='ALA', numeric='248', apolitical_name='Åland Islands', flag='🇦🇽'),
  'ALBANIA': Country(name='Albania', alpha2='AL', alpha3='ALB', numeric='008', apolitical_name='Albania', flag='🇦🇱'), 'ALGERIA': Country(name='Algeria', alpha2='DZ', alpha3='DZA', numeric='012', apolitical_name='Algeria', flag='🇩🇿'),
  ...

  >>> iso3166.countries_by_numeric
  >>> {'004': Country(name='Afghanistan', alpha2='AF', alpha3='AFG', numeric='004', apolitical_name='Afghanistan', flag='🇦🇫'),
  '008': Country(name='Albania', alpha2='AL', alpha3='ALB', numeric='008', apolitical_name='Albania', flag='🇦🇱'),
  '010': Country(name='Antarctica', alpha2='AQ', alpha3='ATA', numeric='010', apolitical_name='Antarctica', flag='🇦🇶'),
  ...

  >>> iso3166.countries_by_alpha2
  >>> {'AD': Country(name='Andorra', alpha2='AD', alpha3='AND', numeric='020', apolitical_name='Andorra', flag='🇦🇩'),
  'AE': Country(name='United Arab Emirates', alpha2='AE', alpha3='ARE', numeric='784', apolitical_name='United Arab Emirates', flag='🇦🇪'),
  'AF': Country(name='Afghanistan', alpha2='AF', alpha3='AFG', numeric='004', apolitical_name='Afghanistan', flag='🇦🇫'),
  ...

  >>> iso3166.countries_by_alpha3
  >>> {'ABW': Country(name='Aruba', alpha2='AW', alpha3='ABW', numeric='533', apolitical_name='Aruba', flag='🇦🇼'),
  'AFG': Country(name='Afghanistan', alpha2='AF', alpha3='AFG', numeric='004', apolitical_name='Afghanistan', flag='🇦🇫'),
  'AGO': Country(name='Angola', alpha2='AO', alpha3='AGO', numeric='024', apolitical_name='Angola', flag='🇦🇴'),
  ...
