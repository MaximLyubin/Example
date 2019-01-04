# coding: utf-8
from horoscope import generate_prophecies
from datetime import datetime as dt

def generate_page (head, body):
    page = f"<html>{head}{body}</html>"
    return page

def generate_head (title):
    head = f"""<head>
	<meta charset=utf-8>
	<title> {title}</title>
	</head>"""
    return head

def generate_body (header, paragraphs):
    body = f"<h1>{header}</h1>"
    for p in paragraphs:
        body = body + f"<p>{p}</p>"
    
    body = body + f"<hr><a href=\"about.html\">О реализации</a>"
    return f"<body>{body}</body>"

def generate_about_page_body(header, paragraphs,picture):
    body = f"<h1>{header}</h1>"
    body = body + f"<img src=\"{picture}\" width=\"100\">"
    body = body +"<ol><li>Времена дня:</li><ul><li>Утром</li><li>Вечером</li><li>После обеда</li></ul><li>Глаголы:</li><ul><li>остерегайтесь</li><li>ожидайте</li></ul></ol>"
    body = body + f"<a href=\"index.html\">Главная</a>"
    return f"<body>{body}</body>"

def save_page (title, header, paragraphs, output):
    fp = open (output, "w")
    today = dt.now().date()
    page = generate_page (head=generate_head(title), body = generate_body(header=header, paragraphs=paragraphs))
    print(page, file=fp)
    fp.close()

def save_about_page (title, header, paragraphs, picture, output):
    fp = open (output, "w")
    today = dt.now().date()
    page = generate_page (head=generate_head(title), body = generate_about_page_body(header=header, paragraphs=paragraphs, picture=picture))
    print(page, file=fp)
    fp.close()

   

today = dt.now().date()
save_page (title="Гороскоп на сегодня", header="Ваши пресказания на " + str(today), paragraphs=generate_prophecies(),output = "index.html")

save_about_page(title="О реализации",header="О чем все это",paragraphs= "", picture = "horoscope_pic.jpg", output = "about.html")


