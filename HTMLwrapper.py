__author__ = 'pilicurg@GitHub'
__link__="https://github.com/pilicurg/HTMLwrapper"

class HtmlWrapper(object):
    def __init__(self):
        self.name = 'HTML Wrapper Page'
        self.css = self._get_css()

    def _wrap(self, tag, content, **attribs):
        return '<' + \
               tag + \
               ''.join([' ' + k + '=' + v for k, v in attribs.iteritems()]) + \
               '>' + \
               content + \
               '</' + \
               tag + \
               '>'

    def generate(self, filename='./Test.html'):
        with open(filename, 'w') as f:
            f.write(self._wrap('html', self._head() + self._body()))

    def _head(self):
        return self._wrap('head', self._page_title() + self._meta() + self._style())

    def _title(self):
        return self.name

    def _meta(self):
        return '<meta name="Author" content="{}">\n'.format(__author__)

    def _page_title(self):
        return self._wrap('title', self._title())

    def _style(self):
        return self._wrap('style', self.css)

    def _body(self):
        return self._wrap('body', self._header() + self._wrapper() + self._footer())

    def _wrapper(self):
        return self._wrap('div',
                    self._section('Main Body',
                        self._wrap('p', 'This is the main body of the page.')+
                        self._wrap('p', self._wrap('a', 'Link to my GitHub Page', href=__link__))),Class='wrapper')

    def _section(self, title, content, **attribs):
        return self._wrap('div', self._wrap('h3', title) + content, Class='section', **attribs)

    def _header(self):
        return self._wrap('div',
                          self._wrap('div', self._wrap('h1', self._title()), Class='title'), Class='topbar')

    def _get_css(self, filename='./style.css'):
        with open(filename) as css:
            return css.read()

    def _footer(self):
        return self._wrap('div', self._wrap('a', __author__,href=__link__), Class="footer")


if __name__ == '__main__':
    h = HtmlWrapper()
    h.generate()
