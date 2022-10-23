import nltk
from nltk import ChartParser
import os

print(os.path.join(os.getcwd(), 'utapis_sintaksis_kalimat_v2.cfg'))
utapis_grammar = nltk.data.load('file:' + os.path.join(os.getcwd(), 'utapis_sintaksis_kalimat_v2.cfg'), 'cfg')
print(utapis_grammar.start())

def initialize_chart_parser(grammar):
    return ChartParser(grammar)

def parse_tokenized_sentence(parser, sentence_list):
    generator = parser.parse(sentence_list)
    
    generator_content = []
    
    generator_content_num = 0
    for content in generator:
        if generator_content_num > 20:
            break
        generator_content_num += 1
        generator_content.append(content)

    if len(generator_content) <= 0:
        print('Sintaksis kalimat ini SALAH.')

    elif len(generator_content) > 0:
        print('Sintaksis kalimat ini BENAR.')

    for i in generator_content:
        print(i)

utapis_cp = initialize_chart_parser(utapis_grammar)

test_kalimat_benar = ['<nomina>', '<verba>', '<nomina>', '<td_akhir_kal>']
parse_tokenized_sentence(utapis_cp, test_kalimat_benar)

test_kalimat_benar = [
    '<kutip_awal>', '<td_koma>', '<kutip_akhir>', '<verba>', '<nomina>',
    '<nomina>', '<nomina>', '<nomina>', '<nomina>', '<td_koma>',
    '<nomina>', '<nomina>', '<preposisi>', '<nomina>', '<td_koma>',
    '<nomina>', '<kurung_buka>', '<numeralia>', '<kurung_tutup>', 
    '<td_akhir_kal>'
]
parse_tokenized_sentence(utapis_cp, test_kalimat_benar)