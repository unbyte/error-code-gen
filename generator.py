import pandas as pd
import jinja2 as t

templates = t.Environment(loader=t.FileSystemLoader(searchpath="./"))


def render_typescript(data: pd.DataFrame) -> str:
    return _render_template(data, 'templates/ts.tpl')


def _render_template(data: pd.DataFrame, template_path) -> str:
    renderer = templates.get_template(template_path)
    return renderer.render(data=data)
