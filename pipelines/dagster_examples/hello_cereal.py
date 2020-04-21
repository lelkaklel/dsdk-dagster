import os
import csv

from dagster import execute_pipeline, execute_solid, pipeline, solid


@solid
def hello_cereal(context):
    # Assuming the dataset is in the same directory as this file

    dataset_path = os.path.join(os.path.abspath("."), "dagster_examples/cereal.csv")
    context.log.info(dataset_path)
    with open(dataset_path, "r") as fd:
        # Read the rows in using the standard csv library
        cereals = [row for row in csv.DictReader(fd)]
    n = len(cereals)
    context.log.info(f"Found {n} cereals")

    return cereals


@pipeline
def hello_cereal_pipeline():
    hello_cereal()


if __name__ == "__main__":
    result = execute_pipeline(hello_cereal_pipeline)
    assert result.success


def test_hello_cereal_solid():
    res = execute_solid(hello_cereal)
    assert res.success
    assert len(res.output_value()) == 77


def test_hello_cereal_pipeline():
    res = execute_pipeline(hello_cereal_pipeline)
    assert res.success
    assert len(res.result_for_solid("hello_cereal").output_value()) == 77
