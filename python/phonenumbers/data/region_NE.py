"""Auto-generated file, do not edit by hand. NE metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_NE = PhoneMetadata(id='NE', country_code=227, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[029]\d{7}', possible_number_pattern=u'\d{8}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'2(?:0(?:20|3[1-7]|4[134]|5[14]|6[14578]|7[1-578])|1(?:4[145]|5[14]|6[14-68]|7[169]|88))\d{4}', possible_number_pattern=u'\d{8}', example_number=u'20201234'),
    mobile=PhoneNumberDesc(national_number_pattern=u'9[03467]\d{6}', possible_number_pattern=u'\d{8}', example_number=u'93123456'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'08\d{6}', possible_number_pattern=u'\d{8}', example_number=u'08123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'09\d{6}', possible_number_pattern=u'\d{8}', example_number=u'09123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='([029]\d)(\d{2})(\d{2})(\d{2})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['[29]|09']),
        NumberFormat(pattern='(08)(\d{3})(\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['08'])],
    leading_zero_possible=True)