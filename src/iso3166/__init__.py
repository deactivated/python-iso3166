# -*- coding: utf-8 -*-

import re
from typing import Dict, Iterator, NamedTuple, Type, TypeVar, Union, overload

__all__ = ["countries"]

StrOrInt = Union[str, int]
_D = TypeVar("_D")


class Country(NamedTuple):
    name: str
    alpha2: str
    alpha3: str
    numeric: str
    phone_code: str
    apolitical_name: str

_records = [
    Country("Afghanistan", "AF", "AFG", "004", "+93", "Afghanistan"),
    Country("Åland Islands", "AX", "ALA", "248", "+358 (AX)", "Åland Islands"),
    Country("Albania", "AL", "ALB", "008", "+355", "Albania"),
    Country("Algeria", "DZ", "DZA", "012", "+213", "Algeria"),
    Country("American Samoa", "AS", "ASM", "016", "+1-684", "American Samoa"),
    Country("Andorra", "AD", "AND", "020", "+376", "Andorra"),
    Country("Angola", "AO", "AGO", "024", "+244", "Angola"),
    Country("Anguilla", "AI", "AIA", "660", "+1-264", "Anguilla"),
    Country("Antarctica", "AQ", "ATA", "010", "+672", "Antarctica"),
    Country("Antigua and Barbuda", "AG", "ATG", "028", "+1-268", "Antigua and Barbuda"),
    Country("Argentina", "AR", "ARG", "032", "+54", "Argentina"),
    Country("Armenia", "AM", "ARM", "051", "+374", "Armenia"),
    Country("Aruba", "AW", "ABW", "533", "+297", "Aruba"),
    Country("Australia", "AU", "AUS", "036", "+61", "Australia"),
    Country("Austria", "AT", "AUT", "040", "+43", "Austria"),
    Country("Azerbaijan", "AZ", "AZE", "031", "+994", "Azerbaijan"),
    Country("Bahamas", "BS", "BHS", "044", "+1-242", "Bahamas"),
    Country("Bahrain", "BH", "BHR", "048", "+973", "Bahrain"),
    Country("Bangladesh", "BD", "BGD", "050", "+880", "Bangladesh"),
    Country("Barbados", "BB", "BRB", "052", "+1-246", "Barbados"),
    Country("Belarus", "BY", "BLR", "112", "+375", "Belarus"),
    Country("Belgium", "BE", "BEL", "056", "+32", "Belgium"),
    Country("Belize", "BZ", "BLZ", "084", "+501", "Belize"),
    Country("Benin", "BJ", "BEN", "204", "+229", "Benin"),
    Country("Bermuda", "BM", "BMU", "060", "+1-441", "Bermuda"),
    Country("Bhutan", "BT", "BTN", "064", "+975", "Bhutan"),
    Country(
        "Bolivia, Plurinational State of",
        "BO",
        "BOL",
        "068",
        "+591",
        "Bolivia, Plurinational State of",
    ),
    Country(
        "Bonaire, Sint Eustatius and Saba",
        "BQ",
        "BES",
        "535",
        "+599 (BQ)",
        "Bonaire, Sint Eustatius and Saba",
    ),
    Country(
        "Bosnia and Herzegovina", "BA", "BIH", "070", "+387", "Bosnia and Herzegovina"
    ),
    Country("Botswana", "BW", "BWA", "072", "+267", "Botswana"),
    Country("Bouvet Island", "BV", "BVT", "074", "+55 (BV)", "Bouvet Island"),
    Country("Brazil", "BR", "BRA", "076", "+55", "Brazil"),
    Country(
        "British Indian Ocean Territory",
        "IO",
        "IOT",
        "086",
        "+246", 
        "British Indian Ocean Territory",
    ),
    Country("Brunei Darussalam", "BN", "BRN", "096", "+673", "Brunei Darussalam"),
    Country("Bulgaria", "BG", "BGR", "100", "+359", "Bulgaria"),
    Country("Burkina Faso", "BF", "BFA", "854", "+226", "Burkina Faso"),
    Country("Burundi", "BI", "BDI", "108", "+257", "Burundi"),
    Country("Cambodia", "KH", "KHM", "116", "+855", "Cambodia"),
    Country("Cameroon", "CM", "CMR", "120", "+237", "Cameroon"),
    Country("Canada", "CA", "CAN", "124", "+1 (CA)", "Canada"),
    Country("Cabo Verde", "CV", "CPV", "132", "+238", "Cabo Verde"),
    Country("Cayman Islands", "KY", "CYM", "136", "+1-345", "Cayman Islands"),
    Country(
        "Central African Republic",
        "CF",
        "CAF",
        "140",
        "+236", 
        "Central African Republic",
    ),
    Country("Chad", "TD", "TCD", "148", "+235", "Chad"),
    Country("Chile", "CL", "CHL", "152", "+56", "Chile"),
    Country("China", "CN", "CHN", "156", "+86", "China"),
    Country("Christmas Island", "CX", "CXR", "162", "+61 (CX)", "Christmas Island"),
    Country(
        "Cocos (Keeling) Islands",
        "CC",
        "CCK",
        "166",
        "+61 (CC)", 
        "Cocos (Keeling) Islands",
    ),
    Country("Colombia", "CO", "COL", "170", "+57", "Colombia"),
    Country("Comoros", "KM", "COM", "174", "+269", "Comoros"),
    Country("Congo", "CG", "COG", "178", "+242", "Congo"),
    Country(
        "Congo, Democratic Republic of the",
        "CD",
        "COD",
        "180",
        "+243", 
        "Congo, Democratic Republic of the",
    ),
    Country("Cook Islands", "CK", "COK", "184", "+682", "Cook Islands"),
    Country("Costa Rica", "CR", "CRI", "188", "+506", "Costa Rica"),
    Country("Côte d'Ivoire", "CI", "CIV", "384", "+225", "Côte d'Ivoire"),
    Country("Croatia", "HR", "HRV", "191", "+385", "Croatia"),
    Country("Cuba", "CU", "CUB", "192", "+53", "Cuba"),
    Country("Curaçao", "CW", "CUW", "531", "+599", "Curaçao"),
    Country("Cyprus", "CY", "CYP", "196", "+357", "Cyprus"),
    Country("Czechia", "CZ", "CZE", "203", "+420", "Czechia"),
    Country("Denmark", "DK", "DNK", "208", "+45", "Denmark"),
    Country("Djibouti", "DJ", "DJI", "262", "+253", "Djibouti"),
    Country("Dominica", "DM", "DMA", "212", "+1-767", "Dominica"),
    Country("Dominican Republic", "DO", "DOM", "214", "+1-809", "Dominican Republic"),
    Country("Ecuador", "EC", "ECU", "218", "+593", "Ecuador"),
    Country("Egypt", "EG", "EGY", "818", "+20", "Egypt"),
    Country("El Salvador", "SV", "SLV", "222", "+503", "El Salvador"),
    Country("Equatorial Guinea", "GQ", "GNQ", "226", "+240", "Equatorial Guinea"),
    Country("Eritrea", "ER", "ERI", "232", "+291", "Eritrea"),
    Country("Estonia", "EE", "EST", "233", "+372", "Estonia"),
    Country("Ethiopia", "ET", "ETH", "231", "+251", "Ethiopia"),
    Country(
        "Falkland Islands (Malvinas)",
        "FK",
        "FLK",
        "238",
        "+500", 
        "Falkland Islands (Malvinas)",
    ),
    Country("Faroe Islands", "FO", "FRO", "234", "+298", "Faroe Islands"),
    Country("Fiji", "FJ", "FJI", "242", "+679", "Fiji"),
    Country("Finland", "FI", "FIN", "246", "+358", "Finland"),
    Country("France", "FR", "FRA", "250", "+33", "France"),
    Country("French Guiana", "GF", "GUF", "254", "+594", "French Guiana"),
    Country("French Polynesia", "PF", "PYF", "258", "+689", "French Polynesia"),
    Country(
        "French Southern Territories",
        "TF",
        "ATF",
        "260",
        "+262 (TF)", 
        "French Southern Territories",
    ),
    Country("Gabon", "GA", "GAB", "266", "+241", "Gabon"),
    Country("Gambia", "GM", "GMB", "270", "+220", "Gambia"),
    Country("Georgia", "GE", "GEO", "268", "+995", "Georgia"),
    Country("Germany", "DE", "DEU", "276", "+49", "Germany"),
    Country("Ghana", "GH", "GHA", "288", "+233", "Ghana"),
    Country("Gibraltar", "GI", "GIB", "292", "+350", "Gibraltar"),
    Country("Greece", "GR", "GRC", "300", "+30", "Greece"),
    Country("Greenland", "GL", "GRL", "304", "+299", "Greenland"),
    Country("Grenada", "GD", "GRD", "308", "+1-473", "Grenada"),
    Country("Guadeloupe", "GP", "GLP", "312", "+590", "Guadeloupe"),
    Country("Guam", "GU", "GUM", "316", "+1-502", "Guam"),
    Country("Guatemala", "GT", "GTM", "320", "+502", "Guatemala"),
    Country("Guernsey", "GG", "GGY", "831", "+44-1481", "Guernsey"),
    Country("Guinea", "GN", "GIN", "324", "+224", "Guinea"),
    Country("Guinea-Bissau", "GW", "GNB", "624", "+245", "Guinea-Bissau"),
    Country("Guyana", "GY", "GUY", "328", "+592", "Guyana"),
    Country("Haiti", "HT", "HTI", "332", "+509", "Haiti"),
    Country(
        "Heard Island and McDonald Islands",
        "HM",
        "HMD",
        "334",
        "+672 (HM)", 
        "Heard Island and McDonald Islands",
    ),
    Country("Holy See", "VA", "VAT", "336", "+379", "Holy See"),
    Country("Honduras", "HN", "HND", "340", "+504", "Honduras"),
    Country("Hong Kong", "HK", "HKG", "344", "+852", "Hong Kong"),
    Country("Hungary", "HU", "HUN", "348", "+36", "Hungary"),
    Country("Iceland", "IS", "ISL", "352", "+354", "Iceland"),
    Country("India", "IN", "IND", "356", "+91", "India"),
    Country("Indonesia", "ID", "IDN", "360", "+62", "Indonesia"),
    Country(
        "Iran, Islamic Republic of",
        "IR",
        "IRN",
        "364",
        "+98", 
        "Iran, Islamic Republic of",
    ),
    Country("Iraq", "IQ", "IRQ", "368", "+964", "Iraq"),
    Country("Ireland", "IE", "IRL", "372", "+353", "Ireland"),
    Country("Isle of Man", "IM", "IMN", "833", "+44-1624", "Isle of Man"),
    Country("Israel", "IL", "ISR", "376", "+972", "Israel"),
    Country("Italy", "IT", "ITA", "380", "+39", "Italy"),
    Country("Jamaica", "JM", "JAM", "388", "+1-876", "Jamaica"),
    Country("Japan", "JP", "JPN", "392", "+81", "Japan"),
    Country("Jersey", "JE", "JEY", "832", "+44-1534", "Jersey"),
    Country("Jordan", "JO", "JOR", "400", "+962", "Jordan"),
    Country("Kazakhstan", "KZ", "KAZ", "398", "+997", "Kazakhstan"),
    Country("Kenya", "KE", "KEN", "404", "+254", "Kenya"),
    Country("Kiribati", "KI", "KIR", "296", "+686", "Kiribati"),
    Country(
        "Korea, Democratic People's Republic of",
        "KP",
        "PRK",
        "408",
        "+850", 
        "Korea, Democratic People's Republic of",
    ),
    Country("Korea, Republic of", "KR", "KOR", "410", "+82", "Korea, Republic of"),
    Country("Kosovo", "XK", "XKX", "983", "+383", "Kosovo"),
    Country("Kuwait", "KW", "KWT", "414", "+965", "Kuwait"),
    Country("Kyrgyzstan", "KG", "KGZ", "417", "+996", "Kyrgyzstan"),
    Country(
        "Lao People's Democratic Republic",
        "LA",
        "LAO",
        "418",
        "+856", 
        "Lao People's Democratic Republic",
    ),
    Country("Latvia", "LV", "LVA", "428", "+371", "Latvia"),
    Country("Lebanon", "LB", "LBN", "422", "+961", "Lebanon"),
    Country("Lesotho", "LS", "LSO", "426", "+266", "Lesotho"),
    Country("Liberia", "LR", "LBR", "430", "+231", "Liberia"),
    Country("Libya", "LY", "LBY", "434", "+218", "Libya"),
    Country("Liechtenstein", "LI", "LIE", "438", "+423", "Liechtenstein"),
    Country("Lithuania", "LT", "LTU", "440", "+370", "Lithuania"),
    Country("Luxembourg", "LU", "LUX", "442", "+352", "Luxembourg"),
    Country("Macao", "MO", "MAC", "446", "+853", "Macao"),
    Country("North Macedonia", "MK", "MKD", "807", "+389", "North Macedonia"),
    Country("Madagascar", "MG", "MDG", "450", "+261", "Madagascar"),
    Country("Malawi", "MW", "MWI", "454", "+265", "Malawi"),
    Country("Malaysia", "MY", "MYS", "458", "+60", "Malaysia"),
    Country("Maldives", "MV", "MDV", "462", "+960", "Maldives"),
    Country("Mali", "ML", "MLI", "466", "+223", "Mali"),
    Country("Malta", "MT", "MLT", "470", "+356", "Malta"),
    Country("Marshall Islands", "MH", "MHL", "584", "+692", "Marshall Islands"),
    Country("Martinique", "MQ", "MTQ", "474", "+596", "Martinique"),
    Country("Mauritania", "MR", "MRT", "478", "+222", "Mauritania"),
    Country("Mauritius", "MU", "MUS", "480", "+230", "Mauritius"),
    Country("Mayotte", "YT", "MYT", "175", "+262", "Mayotte"),
    Country("Mexico", "MX", "MEX", "484", "+52", "Mexico"),
    Country(
        "Micronesia, Federated States of",
        "FM",
        "FSM",
        "583",
        "+691", 
        "Micronesia, Federated States of",
    ),
    Country(
        "Moldova, Republic of", "MD", "MDA", "498", "+373", "Moldova, Republic of"
    ),
    Country("Monaco", "MC", "MCO", "492", "+377", "Monaco"),
    Country("Mongolia", "MN", "MNG", "496", "+976", "Mongolia"),
    Country("Montenegro", "ME", "MNE", "499", "+382", "Montenegro"),
    Country("Montserrat", "MS", "MSR", "500", "+1-664", "Montserrat"),
    Country("Morocco", "MA", "MAR", "504", "+212", "Morocco"),
    Country("Mozambique", "MZ", "MOZ", "508", "+258", "Mozambique"),
    Country("Myanmar", "MM", "MMR", "104", "+95", "Myanmar"),
    Country("Namibia", "NA", "NAM", "516", "+264", "Namibia"),
    Country("Nauru", "NR", "NRU", "520", "+674", "Nauru"),
    Country("Nepal", "NP", "NPL", "524", "+977", "Nepal"),
    Country("Netherlands", "NL", "NLD", "528", "+31", "Netherlands"),
    Country("New Caledonia", "NC", "NCL", "540", "+687", "New Caledonia"),
    Country("New Zealand", "NZ", "NZL", "554", "+64", "New Zealand"),
    Country("Nicaragua", "NI", "NIC", "558", "+505", "Nicaragua"),
    Country("Niger", "NE", "NER", "562", "+227", "Niger"),
    Country("Nigeria", "NG", "NGA", "566", "+234", "Nigeria"),
    Country("Niue", "NU", "NIU", "570", "+683", "Niue"),
    Country("Norfolk Island", "NF", "NFK", "574", "+672 (NF)", "Norfolk Island"),
    Country(
        "Northern Mariana Islands",
        "MP",
        "MNP",
        "580",
        "+1-670", 
        "Northern Mariana Islands",
    ),
    Country("Norway", "NO", "NOR", "578", "+47", "Norway"),
    Country("Oman", "OM", "OMN", "512", "+968", "Oman"),
    Country("Pakistan", "PK", "PAK", "586", "+92", "Pakistan"),
    Country("Palau", "PW", "PLW", "585", "+680", "Palau"),
    Country("Palestine, State of", "PS", "PSE", "275", "+970", "Palestine"),
    Country("Panama", "PA", "PAN", "591", "+507", "Panama"),
    Country("Papua New Guinea", "PG", "PNG", "598", "+675", "Papua New Guinea"),
    Country("Paraguay", "PY", "PRY", "600", "+595", "Paraguay"),
    Country("Peru", "PE", "PER", "604", "+51", "Peru"),
    Country("Philippines", "PH", "PHL", "608", "+63", "Philippines"),
    Country("Pitcairn", "PN", "PCN", "612", "+64 (PN)", "Pitcairn"),
    Country("Poland", "PL", "POL", "616", "+48", "Poland"),
    Country("Portugal", "PT", "PRT", "620", "+351", "Portugal"),
    Country("Puerto Rico", "PR", "PRI", "630", "+1-787", "Puerto Rico"),
    Country("Qatar", "QA", "QAT", "634", "+974", "Qatar"),
    Country("Réunion", "RE", "REU", "638", "+262 (RE)", "Réunion"),
    Country("Romania", "RO", "ROU", "642", "+40", "Romania"),
    Country("Russian Federation", "RU", "RUS", "643", "+7", "Russian Federation"),
    Country("Rwanda", "RW", "RWA", "646", "+250", "Rwanda"),
    Country("Saint Barthélemy", "BL", "BLM", "652", "+590 (BL)", "Saint Barthélemy"),
    Country(
        "Saint Helena, Ascension and Tristan da Cunha",
        "SH",
        "SHN",
        "654",
        "+290", 
        "Saint Helena, Ascension and Tristan da Cunha",
    ),
    Country(
        "Saint Kitts and Nevis", "KN", "KNA", "659", "+1-869", "Saint Kitts and Nevis"
    ),
    Country("Saint Lucia", "LC", "LCA", "662", "+1-758", "Saint Lucia"),
    Country(
        "Saint Martin (French part)",
        "MF",
        "MAF",
        "663",
        "+590 (MF)",
        "Saint Martin (French part)",
    ),
    Country(
        "Saint Pierre and Miquelon",
        "PM",
        "SPM",
        "666",
        "+508", 
        "Saint Pierre and Miquelon",
    ),
    Country(
        "Saint Vincent and the Grenadines",
        "VC",
        "VCT",
        "670",
        "+1-784", 
        "Saint Vincent and the Grenadines",
    ),
    Country("Samoa", "WS", "WSM", "882", "+685", "Samoa"),
    Country("San Marino", "SM", "SMR", "674", "+378", "San Marino"),
    Country(
        "Sao Tome and Principe", "ST", "STP", "678", "+239", "Sao Tome and Principe"
    ),
    Country("Saudi Arabia", "SA", "SAU", "682", "+966", "Saudi Arabia"),
    Country("Senegal", "SN", "SEN", "686", "+221", "Senegal"),
    Country("Serbia", "RS", "SRB", "688", "+381", "Serbia"),
    Country("Seychelles", "SC", "SYC", "690", "248+", "Seychelles"),
    Country("Sierra Leone", "SL", "SLE", "694", "+232", "Sierra Leone"),
    Country("Singapore", "SG", "SGP", "702", "+65", "Singapore"),
    Country(
        "Sint Maarten (Dutch part)",
        "SX",
        "SXM",
        "534",
        "+1-721", 
        "Sint Maarten (Dutch part)",
    ),
    Country("Slovakia", "SK", "SVK", "703", "+421", "Slovakia"),
    Country("Slovenia", "SI", "SVN", "705", "+386", "Slovenia"),
    Country("Solomon Islands", "SB", "SLB", "090", "+677", "Solomon Islands"),
    Country("Somalia", "SO", "SOM", "706", "+252", "Somalia"),
    Country("South Africa", "ZA", "ZAF", "710", "+27", "South Africa"),
    Country(
        "South Georgia and the South Sandwich Islands",
        "GS",
        "SGS",
        "239",
        "+500 (GS)", 
        "South Georgia and the South Sandwich Islands",
    ),
    Country("South Sudan", "SS", "SSD", "728", "+211", "South Sudan"),
    Country("Spain", "ES", "ESP", "724", "+34", "Spain"),
    Country("Sri Lanka", "LK", "LKA", "144", "+94", "Sri Lanka"),
    Country("Sudan", "SD", "SDN", "729", "+249", "Sudan"),
    Country("Suriname", "SR", "SUR", "740", "+597", "Suriname"),
    Country(
        "Svalbard and Jan Mayen", "SJ", "SJM", "744", "+47 (SJ)", "Svalbard and Jan Mayen"
    ),
    Country("Eswatini", "SZ", "SWZ", "748", "+268", "Eswatini"),
    Country("Sweden", "SE", "SWE", "752", "+46", "Sweden"),
    Country("Switzerland", "CH", "CHE", "756", "+41", "Switzerland"),
    Country(
        "Syrian Arab Republic", "SY", "SYR", "760", "+963", "Syrian Arab Republic"
    ),
    Country("Taiwan, Province of China", "TW", "TWN", "158", "+886", "Taiwan"),
    Country("Tajikistan", "TJ", "TJK", "762", "+992", "Tajikistan"),
    Country(
        "Tanzania, United Republic of",
        "TZ",
        "TZA",
        "834",
        "+255", 
        "Tanzania, United Republic of",
    ),
    Country("Thailand", "TH", "THA", "764", "+66", "Thailand"),
    Country("Timor-Leste", "TL", "TLS", "626", "+670", "Timor-Leste"),
    Country("Togo", "TG", "TGO", "768", "+228", "Togo"),
    Country("Tokelau", "TK", "TKL", "772", "+690", "Tokelau"),
    Country("Tonga", "TO", "TON", "776", "+676", "Tonga"),
    Country("Trinidad and Tobago", "TT", "TTO", "780", "+1-868", "Trinidad and Tobago"),
    Country("Tunisia", "TN", "TUN", "788", "+216", "Tunisia"),
    Country("Türkiye", "TR", "TUR", "792", "+90", "Türkiye"),
    Country("Turkmenistan", "TM", "TKM", "795", "+993", "Turkmenistan"),
    Country(
        "Turks and Caicos Islands",
        "TC",
        "TCA",
        "796",
        "+1-649", 
        "Turks and Caicos Islands",
    ),
    Country("Tuvalu", "TV", "TUV", "798", "+688", "Tuvalu"),
    Country("Uganda", "UG", "UGA", "800", "+256", "Uganda"),
    Country("Ukraine", "UA", "UKR", "804", "+380", "Ukraine"),
    Country(
        "United Arab Emirates", "AE", "ARE", "784", "+971", "United Arab Emirates"
    ),
    Country(
        "United Kingdom of Great Britain and Northern Ireland",
        "GB",
        "GBR",
        "826",
        "+44", 
        "United Kingdom of Great Britain and Northern Ireland",
    ),
    Country(
        "United States of America",
        "US",
        "USA",
        "840",
        "+1", 
        "United States of America",
    ),
    Country(
        "United States Minor Outlying Islands",
        "UM",
        "UMI",
        "581",
        "+1 (UM)", 
        "United States Minor Outlying Islands",
    ),
    Country("Uruguay", "UY", "URY", "858", "+598", "Uruguay"),
    Country("Uzbekistan", "UZ", "UZB", "860", "+998", "Uzbekistan"),
    Country("Vanuatu", "VU", "VUT", "548", "+678", "Vanuatu"),
    Country(
        "Venezuela, Bolivarian Republic of",
        "VE",
        "VEN",
        "862",
        "+58", 
        "Venezuela, Bolivarian Republic of",
    ),
    Country("Viet Nam", "VN", "VNM", "704", "+84", "Viet Nam"),
    Country(
        "Virgin Islands, British",
        "VG",
        "VGB",
        "092",
        "+1-248", 
        "Virgin Islands, British",
    ),
    Country(
        "Virgin Islands, U.S.", "VI", "VIR", "850", "+1-340", "Virgin Islands, U.S."
    ),
    Country("Wallis and Futuna", "WF", "WLF", "876", "+681", "Wallis and Futuna"),
    Country("Western Sahara", "EH", "ESH", "732", "+212 (EH)", "Western Sahara"),
    Country("Yemen", "YE", "YEM", "887", "+967", "Yemen"),
    Country("Zambia", "ZM", "ZMB", "894", "+260", "Zambia"),
    Country("Zimbabwe", "ZW", "ZWE", "716", "+263", "Zimbabwe"),
]


def _build_index(idx: int) -> Dict[str, Country]:
    return dict((r[idx].upper(), r) for r in _records)


# Internal country indexes
_by_alpha2 = _build_index(1)
_by_alpha3 = _build_index(2)
_by_numeric = _build_index(3)
_by_name = _build_index(0)
_by_phone_code = _build_index(4)
_by_apolitical_name = _build_index(5)


# Documented accessors for the country indexes
countries_by_alpha2 = _by_alpha2
countries_by_alpha3 = _by_alpha3
countries_by_numeric = _by_numeric
countries_by_name = _by_name
countries_by_phone_code = _by_phone_code
countries_by_apolitical_name = _by_apolitical_name


class NotFound:
    pass


class _CountryLookup:
    @overload
    def get(self, key: StrOrInt) -> Country:
        ...

    @overload
    def get(self, key: StrOrInt, default: _D) -> Union[Country, _D]:
        ...

    def get(
        self, key: StrOrInt, default: Union[Type[NotFound], _D] = NotFound
    ) -> Union[Country, _D]:
        if isinstance(key, int):
            k = f"{key:03d}"
            r = _by_numeric.get(k, default)
        else:
            k = key.upper()
            if len(k) >= 2 and k[0] == "+": 
                r = _by_phone_code.get(k, default)
            elif len(k) == 2:
                r = _by_alpha2.get(k, default)
            elif len(k) == 3 and re.match(r"[0-9]{3}", k) and k != "000":
                r = _by_numeric.get(k, default)
            elif len(k) == 3:
                r = _by_alpha3.get(k, default)
            elif k in _by_name:
                r = _by_name.get(k, default)
            else:
                r = _by_apolitical_name.get(k, default)

        if r == NotFound:
            raise KeyError(key)

        return r

    __getitem__ = get

    def __len__(self) -> int:
        return len(_records)

    def __iter__(self) -> Iterator[Country]:
        return iter(_records)

    def __contains__(self, item: StrOrInt) -> bool:
        try:
            self.get(item)
            return True
        except KeyError:
            return False


countries = _CountryLookup()
