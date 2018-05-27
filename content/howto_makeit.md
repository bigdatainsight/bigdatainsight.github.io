Title: How to Generate static blog with Python
Slug: how_to_generate_static_blog_with_python
Category: Markdown
Tags: Pelican, Anaconda, Python, Markdown
Date: 2016-06-08 20:00
Author: me
Summary: This is a demo page to show how Pelican support generating static pages Markdown.



# Installing Pelican

* Install miniconda3
* Create a virtual envrionment with python 2.7, called "pelican"
* Intall pelican and required modules

```bash

pip install -r requirements.txt

```

The content of requirementx.txt is like this:

```bash

pelican==3.7.1
Markdown==2.6.11
jupyter>=1.0.0
ipython>=5.7.0
nbconvert>=5.3.1
beautifulsoup4>=4.6.0
ghp-import==0.5.5
matplotlib==2.2.2
typogrify==2.0.7
fabric==1.14.0

```

# Creating your data science blog

```bash

mkdir bigdatainsight.github.io
cd bigdatainsight.github.io
pelican-quickstart

```

# Installing plugins

In the blog root folder, `bigdatainsight.github.io`, clone pelican plugins.

```bash
git clone https://github.com/getpelican/pelican-plugins.git
```

# Install the Jupyter plugin

In the blog root folder, `bigdatainsight.github.io`, install ipynb plugin as git submodule.

```bash
git submodule add git://github.com/danielfrg/pelican-ipynb.git plugins/ipynb
```

modify `pelicanconf.py` and add these lines at the bottom:

```python
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
```

# Writing your first post

* Jupyter Notebook
  + put a jutyter notebook file in the content directory
  + create a meta file for the notebook
    If the notebook file named `note1.ipynb`, then create a `note1.ipynb-meta` file.

```text
Title: First Post
Slug: first-post
Date: 2016-06-08 20:00
Category: posts
Tags: python firsts
Author: Vik Paruchuri
Summary: My first post, read it to find out.
```

* Markdown file
  + Create a .md file in the content directory

# Generating HTML

In order to generate HTML from our post, we'll need to run Pelican to convert the notebooks to HTML, then run a local server to be able to view them:

* Switch to the `bigdatainsight.github.io` folder.
* Run `pelican content` to generate the HTML.
* Switch to the `output` directory.
* Run `python -m pelican.server`.
* Visit [localhost:8000](localhost:8000) in your browser to preview the blog.

You have to repeat these commands again and again.

```bash
pelican content
cd output
python -m pelican.server
cd ..
```

To make it easier, just use

```bash
fab reserve
```

This is equavalent to above four commands.

# Deploy to GitHub Pages

* Run `ghp-import output -b master` to import everything in the output folder to the master branch.
* Use `git push origin master` to push your content to GitHub.

# Choose a Theme

The Pelican community offers a variety of themes at [pelicanthemes.com](http://www.pelicanthemes.com/).

[PELICAN THEME DEMOS](http://ptd.pronoiac.org) has many screen shots for the themes.

* get pelican themes

```bash
git clone --recursive https://github.com/getpelican/pelican-themes pelican-themes
```

* Create a THEME variable in your `pelicanconf.py` file and set its value to the location of the theme:

```python
THEME = 'C:\\Pelican\\pelican-themes\\flex
```
