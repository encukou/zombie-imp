# zombie-imp

~~A particularly mischevious act of necromancy. That is,~~
A copy of the `imp` module that was removed in Python 3.12.

Don't use this, it'll probably trick and bite you.


# Usage

Can be summoned by `import zombie_imp`.

On Python versions where `imp` was banished, reanimate it using `import imp`.
It promises (with a sneer) to be the same as before.

Some functionality that was severed from `pkgutil` is interred
in `zombie_imp.pkgutil`, ready for reattachment:

- `ImpImporter`
- `ImpLoader`


# Development

You want to help it? Think you'll be rewarded?
Great! It loves gullible brains.

Seriously, **run!**
Find a project that needs this and port *that* to `importlib`.


## License

The code was snatched from CPython, and is available under CPython's license
(SPDX: `Python-2.0.1`).
