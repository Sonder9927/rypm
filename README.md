# rye-rp

python project with rust.

## init

```sh
rye init project --build-system maturin
cd project
rye pin 3.12
rye add --dev pip
# rye install maturin
rye sync
```

## docs

Init docs.

`duties.py`:

```sh
rye add mkdocs mkdocs-material mkdocstrings-python
rye sync
rye run mkdocs new ./
```

Change theme of docs.

`mkdocs.yml`:

```yml
site_name: project
theme: material

nav:
  - Home: index.md
  - python: python.md

plugins:
- search
- mkdocstrings:
    handlers:
      python:
        paths: [python.project]
        options:
          show_source: false
```

Build docs.

```sh
rye run mkdocs build
```
