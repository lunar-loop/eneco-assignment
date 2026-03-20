import typer

app = typer.Typer()


@app.command()
def load_data(catalog_object_name):
    print("Loading data...")
    from src.core.load_data import run_data_load

    run_data_load(catalog_object_name)


@app.command()
def analyze(sql_file, database):
    print("Running analysis...")
    from src.core.analyze import run_analysis

    run_analysis(sql_file, database)


@app.command()
def validate(catalog_object_name):
    print("Validating results...")
    from src.core.validate import run_validation

    run_validation(catalog_object_name)


if __name__ == "__main__":
    app()
