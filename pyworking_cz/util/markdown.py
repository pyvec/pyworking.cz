from functools import lru_cache
from markdown import markdown
import re


@lru_cache()
def markdown_to_html(text):
    html = markdown(
        text,
        extensions=[
            'mdx_urlize',
        ])
    html = fix_preposition_nbsp(html)
    return html


def fix_preposition_nbsp(html):
    return re.sub(r'([ (][svz]) ', r'\1&nbsp;', html, flags=re.IGNORECASE)
