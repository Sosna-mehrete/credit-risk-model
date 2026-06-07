import pytest
from src import data_processing


@pytest.fixture(scope="module")
def processed_df():
    return data_processing.run_pipeline()


def test_feature_columns(processed_df):
    df = processed_df
    assert "customer_id" in df.columns


def test_rfm_generation(processed_df):
    df = processed_df
    assert "recency" in df.columns
    assert "frequency" in df.columns
    assert "monetary" in df.columns