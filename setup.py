from setuptools import setup

requires = [
    'pyramid',
    'pyramid_jinja2',
    'waitress'
]

setup(name='card_validator',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = card_validator:main
      """,
)
