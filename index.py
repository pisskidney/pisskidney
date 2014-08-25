import os
import re
from flask import Flask, render_template, session


app = Flask(__name__)


CLRS_DIR = 'clrs_exercises'
CLRS_CHAPTER_PREFIX = 'chapter_'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/clrs')
def clrs():
    clrs_dir = os.path.join(app.template_folder, CLRS_DIR)
    problems = dict()
    for chapter in os.listdir(clrs_dir):
        _, chapter_id = chapter.split('_')
        for filename in os.listdir(os.path.join(clrs_dir, chapter)):
            m = re.match('([0-9]+)_([0-9]+).html', filename)
            section, problem = m.groups()
            chapter_dict = problems.setdefault(chapter_id, {})
            chapter_dict.setdefault(section, []).append(problem)
    return render_template('clrs.html', problems=problems)


@app.route('/clrs/<c>.<s>-<p>')
def clrs_ex(c, s, p):
    chapter = CLRS_CHAPTER_PREFIX + c
    template_dir = os.path.join(CLRS_DIR, chapter)
    template_path = os.path.join(template_dir, s + '_' + p + '.html')
    return render_template(template_path, ex=c + '.' + s + '-' + p)


if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0')
