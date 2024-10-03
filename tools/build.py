import os
import frontmatter
from string import Template
from markdown import markdown


# notes dir
notedir = '../notes'

# note file list
notes = [f'{notedir}/{note}'
         for note in os.listdir(notedir)]

# site title
site_title = 'RUANG site'

# index template
index_tmpl = '''<!DOCTYPE html>
<html>
<head>
<title>$site_title</title>
<style>
body {
background-color:whitesmoke
}
.article-panel {
background-color: #f9f9f9;
padding: 20px;
border-radius: 5px;
box-shadow: 0 2px 5px rgba(0,0,0,0.1);
margin-bottom: 20px;
}
.article-title {
font-size: 1.5em;
margin-bottom: 10px;
}
.article-date {
color: #777;
margin-bottom: 10px;
}
.article-content {
line-height: 1.6;
}
</style>
</head>
<body>
<h1 style="text-align: left;">$site_title</h1>
<div class="row1">
<p style="text-align: left;">
<a href="http://www.github.com/rruuaanng"><b>github</b></a> |
<a href="notes/"><b>notes</b></a> |
</p>
</div>
<hr><div class="blog">
<ul>
$news_list
</ul>
</div><hr>
</body>
</html>
'''

# news template
news_tmpl = '''
<li class="panel">
<div class="title">$title</div>
<div class="time">$time</div>
<div class="author">$author</div>
<div class="content">
$content
</div>
</li>
'''

def render_news(post_meta, content):
    '''render a news'''
    template = Template(news_tmpl)
    html = template.substitute(title=post_meta.get('title', 'HELLO'),
                               time=post_meta.get('time', '1981/1/1'),
                               author=post_meta.get('author', 'XXX'),
                               content=content)
    return html

def render_index(news_list):
    '''render index'''
    template = Template(index_tmpl)
    return template.substitute(site_title=site_title,
                               news_list=news_list)

def md_converto_html(md_text):
    '''markdown convert to html'''
    return markdown(md_text)

def main():
    news_list = ''
    for note in notes:
        with open(note, 'r') as fp:
            try:
                post = frontmatter.load(fp)
                html = md_converto_html(post.content)
                news_list += f'{render_news(post.metadata, html)}\n'
            except Exception:
                os._exit(1)
    else:
        with open('../index.html', 'w') as fp:
            fp.write(render_index(news_list))

if __name__ == '__main__':
    main()
    os._exit(0)
