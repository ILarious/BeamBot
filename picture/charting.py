from PIL import Image, ImageDraw, ImageFont


async def picture1(value):
    image = Image.open('picture/beam_section_1.png')

    Mq = value['Mq']
    Qq = value['Qq']

    font = ImageFont.truetype("picture/GOST_AI.ttf", 25)

    drawer = ImageDraw.Draw(image)
    drawer.text((380, 275), f'{Mq/100}', font=font, fill='black')
    drawer.text((95, 475), f'{Qq}', font=font, fill='black')
    image.save('picture/user_beam_1.png')


async def picture2(value):
    image = Image.open('picture/beam_section_2.png')

    rb1 = value['rb1']
    ra1 = value['ra1']
    Qp01 = value['Qp01']
    Mp01d = value['Mp01d']

    font = ImageFont.truetype("picture/GOST_AI.ttf", 30)

    drawer = ImageDraw.Draw(image)
    drawer.text((250, 940), f'{rb1}', font=font, fill='black')
    drawer.text((315, 670), f'{ra1}', font=font, fill='black')
    drawer.text((300, 750), f'{Qp01}', font=font, fill='black')
    drawer.text((300, 530), f'{Mp01d}', font=font, fill='black')
    image.save('picture/user_beam_2.png')


async def picture3(value):
    image = Image.open('picture/beam_section_3.png')

    Ra1 = value['Ra1']
    Rb1 = value['Rb1']
    Qp12 = value['Qp12']
    Mp11 = value['Mp11']
    Mp12 = value['Mp12']

    font = ImageFont.truetype("picture/GOST_AI.ttf", 22)

    drawer = ImageDraw.Draw(image)
    drawer.text((20, 440), f'{Ra1}', font=font, fill='black')
    drawer.text((150, 570), f'{Rb1}', font=font, fill='black')
    drawer.text((195, 475), f'{Qp12}', font=font, fill='black')
    drawer.text((58, 300), f'{Mp11}', font=font, fill='black')
    drawer.text((190, 260), f'{Mp12}', font=font, fill='black')
    image.save('picture/user_beam_3.png')



async def picture4(value):

    image = Image.open('picture/beam_section_4.png')

    Ra2 = value['Ra2']
    Rb2 = value['Rb2']
    Qp22 = value['Qp22']
    Mp21 = value['Mp21']
    Mp22 = value['Mp22']

    font = ImageFont.truetype("picture/GOST_AI.ttf", 27)

    drawer = ImageDraw.Draw(image)
    drawer.text((245, 650), f'{Ra2}', font=font, fill='black')
    drawer.text((230, 842), f'{Rb2}', font=font, fill='black')
    drawer.text((350, 720), f'{Qp22}', font=font, fill='black')
    drawer.text((150, 445), f'{Mp21}', font=font, fill='black')
    drawer.text((350, 400), f'{Mp22}', font=font, fill='black')
    image.save('picture/user_beam_4.png')


async def picture5(value):
    image = Image.open('picture/beam_section_5.png')

    Ra3 = value['Ra3']
    Rb3 = value['Rb3']
    Qp32 = value['Qp32']
    Mp31 = value['Mp31']
    Mp32 = value['Mp32']

    font = ImageFont.truetype("picture/GOST_AI.ttf", 22)

    drawer = ImageDraw.Draw(image)
    drawer.text((160, 445), f'{Ra3}', font=font, fill='black')
    drawer.text((145, 580), f'{Rb3}', font=font, fill='black')
    drawer.text((240, 500), f'{Qp32}', font=font, fill='black')
    drawer.text((90, 290), f'{Mp31}', font=font, fill='black')
    drawer.text((240, 260), f'{Mp32}', font=font, fill='black')
    image.save('picture/user_beam_5.png')


async def picture6(value):
    image = Image.open('picture/beam_section_6.png')

    Ra4 = value['Ra4']
    Rb4 = value['Rb4']
    Qp42 = value['Qp42']
    Mp41 = value['Mp41']
    Mp42 = value['Mp42']

    font = ImageFont.truetype("picture/GOST_AI.ttf", 24)

    drawer = ImageDraw.Draw(image)
    drawer.text((210, 580), f'{Ra4}', font=font, fill='black')
    drawer.text((200, 755), f'{Rb4}', font=font, fill='black')
    drawer.text((305, 645), f'{Qp42}', font=font, fill='black')
    drawer.text((125, 390), f'{Mp41}', font=font, fill='black')
    drawer.text((305, 350), f'{Mp42}', font=font, fill='black')
    image.save('picture/user_beam_6.png')


async def picture7(value):
    image = Image.open('picture/beam_section_7.png')

    Ra5 = value['Ra5']
    Rb5 = value['Rb5']
    Mp51 = value['Mp51']

    font = ImageFont.truetype("picture/GOST_AI.ttf", 30)

    drawer = ImageDraw.Draw(image)
    drawer.text((505, 683), f'{Ra5}', font=font, fill='black')
    drawer.text((530, 920), f'{Rb5}', font=font, fill='black')
    drawer.text((650, 450), f'{Mp51}', font=font, fill='black')
    image.save('picture/user_beam_7.png')


async def all_img(value):
    await picture1(value)
    await picture2(value)
    await picture3(value)
    await picture4(value)
    await picture5(value)
    await picture6(value)
    await picture7(value)