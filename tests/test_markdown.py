from pyworking_cz.util import markdown_to_html


def test_markdown_hello_world():
    html = markdown_to_html('Hello, World!')
    assert html == '<p>Hello, World!</p>'


def test_markdown_urlize_urls():
    html = markdown_to_html('See https://pyworking.cz for more info')
    assert html == '<p>See <a href="https://pyworking.cz">https://pyworking.cz</a> for more info</p>'


def test_markdown_prepositions_nbsp():
    html = markdown_to_html('dotazy v SQL, s daty (v prostředí), a dále')
    assert html == '<p>dotazy v&nbsp;SQL, s&nbsp;daty (v&nbsp;prostředí), a dále</p>'
