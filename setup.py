from setuptools  import setup


setup(
  name = 'PersianG2p',         # How you named your package folder (MyLib)
  packages = ['PersianG2p'],   # Chose the same as "name"
  version = '0.2.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Simple grapheme-to-phomene converter for persian (farsi)',   # Give a short description about your library
  author = 'Demetry Pascal',                   # Type in your name
  author_email = 'qtckpuhdsa@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/PasaOpasen/PersianG2P',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/PasaOpasen/PersianG2P/archive/0.2.1.tar.gz',    # I explain this later on
  keywords = ['phonemize', 'g2p', 'persian', 'persian_transcription', 'farsi'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'nltk',
          'numpy',
          'hazm',
          'inflect',
          'num2fawords'
      ],
  include_package_data=True,
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)