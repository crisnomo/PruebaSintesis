import web
from web import form

PORT = 8080

web.config.debug = True
render = web.template.render('templates')

URLS = ("/", "index")

class index():
    form = web.form.Form(
        web.form.Textbox("valor", web.form.notnull, description="Nombre"),
        web.form.Button("Enviar"),
    )

    def GET(self):
        form = self.form()
        return render.index("", form)
    
    def POST(self):
        valor = web.input().get("valor")
        print(valor)
        return render.result(valor)  

app = web.application(URLS, globals())

if __name__ == "__main__":
    app.run()
