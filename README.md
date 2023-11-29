# rye-rp

python project with rust.

# flow

```sh
rye init project --build-system maturin
cd project
rye pin 3.12
rye install maturin
rye add --dev pip
rye sync
maturin develop --skip-install
python python/project
```
