from docxtpl import DocxTemplate, InlineImage
from docx.shared import Cm


async def doc_final(value):
    temp = dict()
    temp.update(value)
    doc = DocxTemplate("Doc_final/шаблон2.docx")
    img_1 = InlineImage(
        doc,
        image_descriptor='picture/user_beam_1.png',
        width=Cm(16),
        height=Cm(16))
    img_2 = InlineImage(
        doc,
        image_descriptor='picture/user_beam_2.png',
        width=Cm(16),
        height=Cm(16))
    img_3 = InlineImage(
        doc,
        image_descriptor='picture/user_beam_3.png',
        width=Cm(16),
        height=Cm(16))
    img_4 = InlineImage(
        doc,
        image_descriptor='picture/user_beam_4.png',
        width=Cm(16),
        height=Cm(16))
    img_5 = InlineImage(
        doc,
        image_descriptor='picture/user_beam_5.png',
        width=Cm(16),
        height=Cm(16))
    img_6 = InlineImage(
        doc,
        image_descriptor='picture/user_beam_6.png',
        width=Cm(16),
        height=Cm(16))
    img_7 = InlineImage(
        doc,
        image_descriptor='picture/user_beam_7.png',
        width=Cm(16),
        height=Cm(16))

    temp['img_1'] = img_1
    temp['img_2'] = img_2
    temp['img_3'] = img_3
    temp['img_4'] = img_4
    temp['img_5'] = img_5
    temp['img_6'] = img_6
    temp['img_7'] = img_7

    doc.render(temp, autoescape=False)
    doc.save("Doc_final/шаблон-final.docx")


    return "Doc_final/шаблон-final.docx"