from functools import lru_cache
from markdown import markdown


@lru_cache()
def markdown_to_html(text):
    html = markdown(
        text,
        extensions=[
            'mdx_urlize',
        ])
    html = html.replace(' v ', ' v&nbsp;')
    html = html.replace(' s ', ' s&nbsp;')
    html = html.replace(' z ', ' z&nbsp;')
    return html
