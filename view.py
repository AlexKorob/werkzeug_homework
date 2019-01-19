import os
from werkzeug.wrappers import Response
from manager import manager
from jinja2 import Environment, FileSystemLoader
from werkzeug.utils import redirect


def validate_add_note(form):
    errors = []
    title = form["title"]
    description = form["description"]
    if not title:
        errors.append('Поле "Название" должно быть заполнено')
    if not description:
        errors.append('Поле "Описание" должно быть заполнено')
    elif len(description) <= 5:
        errors.append('Поле "Описание" должно содержать более 5-ти символов')
    if errors:
        return False, errors
    return True, {}


class View(object):
    def __init__(self):
        template_path = os.path.join(os.path.dirname(__file__), 'templates')
        self.jinja_env = Environment(loader=FileSystemLoader(template_path),
                                     autoescape=True)

    def render_template(self, template_name, **context):
        t = self.jinja_env.get_template(template_name)
        return Response(t.render(context), mimetype='text/html')

    def notes(self, request):
        if request.method == "GET":
            notes = manager.all_notes()
            return self.render_template('notes.html', notes=notes)

    def add_note(self, request):
        errors = []
        if request.method == "POST":
            validate, errors = validate_add_note(request.form)
            title = request.form["title"]
            description = request.form["description"]
            if validate:
                manager.add_note(title=title, description=description)
                return redirect("/")
            return self.render_template("add_note.html", errors=errors, title=title, description=description)
        return self.render_template("add_note.html", errors=errors)

view = View()
