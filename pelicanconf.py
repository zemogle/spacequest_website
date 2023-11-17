AUTHOR = 'Edward Gomez'
SITENAME = 'Space Quest'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'themes/bulma_custom/'

# Blogroll
LINKS = (
        ('Home','/'),
        ('About', '/about/'),
         ('CV', '/curriculum-vitae/'),
         ('Talks', '/talks/'),
)
# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

LANDING_PAGE_TITLE = "Space Quest"

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# We use this to generate the Things list and only the things list 
CATEGORY_SAVE_AS = 'things/index.html'

READERS = {"html": None}