# -*- coding: utf-8 -*-

import pytest
import iso3166


def test_country_list():
    country_list = iso3166.countries
    assert len(country_list) > 100
    assert all(isinstance(c, iso3166.Country) for c in country_list)


def test_by_name():
    table = iso3166.countries_by_name
    assert len(table) >= len(iso3166.countries)
    assert table["AFGHANISTAN"].name == "Afghanistan"


def test_by_number():
    table = iso3166.countries_by_numeric
    assert len(table) >= len(iso3166.countries)
    assert table["008"].name == "Albania"


def test_by_alpha2():
    table = iso3166.countries_by_alpha2
    assert len(table) >= len(iso3166.countries)
    assert table['AE'].name == "United Arab Emirates"


def test_by_alpha3():
    table = iso3166.countries_by_alpha3
    assert len(table) >= len(iso3166.countries)
    assert table['AFG'].name == 'Afghanistan'
