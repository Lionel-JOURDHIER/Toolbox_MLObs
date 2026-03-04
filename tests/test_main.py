from unittest.mock import patch

import pandas as pd

from app.main import get_values_from_csv


def test_get_values_from_csv():
    """Garantit 100% de couverture sur la fonction de lecture."""
    fake_data = {"col1": [1, 2], "col2": [3, 4]}
    fake_df = pd.DataFrame(fake_data)

    with patch("pandas.read_csv") as mock_read:
        mock_read.return_value = fake_df

        result = get_values_from_csv("dummy_path.csv")

        assert isinstance(result, pd.DataFrame)
        assert result.iloc[0, 0] == 1
        mock_read.assert_called_once_with("dummy_path.csv")
