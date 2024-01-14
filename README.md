# rye-rp

python project with rust.

## flow

```sh
rye init project --build-system maturin
cd project
rye pin 3.12
rye install maturin
rye add --dev pip
rye add duty
rye sync
```

## docs

Init docs.

`duties.py`:

```sh
rye add mkdocs mkdocs-material
rye sync
rye run mkdocs new ./
```

Change theme of docs.

`mkdocs.yml`:

```yml
site_name: project
nav:
  - Home: index.md
theme: material
```

Build docs.

```sh
rye run mkdocs build
```
