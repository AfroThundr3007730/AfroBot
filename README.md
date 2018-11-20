AfroBot
=======

This repo hosts the code for [AfroBot](https://en.wikipedia.org/wiki/User:AfroBot), a Wikipedia bot written using the [pywikibot](https://www.mediawiki.org/wiki/Manual:Pywikibot) framework.

It has a modular implementation so that bot tasks can be loaded like "plugins" from the `jobs` directory.

All of the configuration (including job/task configs) will be stored in a `config.json` file.
