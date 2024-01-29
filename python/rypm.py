import marimo

__generated_with = "0.1.86"
app = marimo.App()


@app.cell
def __():
    import marimo as mo
    import rypm
    return mo, rypm


@app.cell
def __(mo):
    mirana = mo.image(src="images/mirana.png")
    mo.md(
        f"""
    # rypm
    {mirana}
    ## Decipt
    Use `rye` to manage `python` + `rust` project. 

    ## repo
    Say `hello` from rust.
    """
    )
    return mirana,


@app.cell
def __(rypm):
    print(rypm.hello())
    return


@app.cell
def __(mo):
    code = mo.ui.code_editor(
        """rye init rypm --build-system maturin
    cd rypm
    rye add mkdocs mkdocs-material mkdocstrings-python marimo
    rye sync"""
    )

    mo.md(
        f"""## Build
    run commands bellow in shell

    {code}
    """
    )
    return code,


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
