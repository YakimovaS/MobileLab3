import docx
from docxtpl import DocxTemplate
from docx2pdf import convert

sot = 717.7
internet = 12.53
summa = sot + internet

doc = DocxTemplate("template.docx") 
context = {
'product' : 'Услуги Сотовой связи',
'qty' : '1',
'price' : sot,
'sum' : sot,
'product1' : 'Оплата Интернет',
'qty1' : '1',
'price1' : internet,
'sum1' : internet,
'fin_sum' : summa,
'fin_nds' : round(summa*20/120.2),
'fin_sum_n' : summa,
'rows' : '2',
'ed' : 'шт',
'string_sum' : 'Семьсот тридцать рублей двадцать три копейки',
'bank' : 'ПАО GoodBank (ИНН 1237083855, ОГРН 1234700132100)',
'inn' : '1234567890',
'kpp': '0987654321',
'supp': 'ООО HaveToPay',
'buyer': 'ООО HaveToBuy',
'director': 'Путин В.В.',
'bik': '12345',
'account': '12345432123563511',
'account2': '02345432123563511',
'doc_num': '5',
'data': '16 апреля 2020',
'base': '№ 202020 от 16.04.2020',
'accountant': 'Главный бухгалтер Медведев Д.А.'
}
doc.render(context) 
doc.save("final.docx") 
convert("final.docx")