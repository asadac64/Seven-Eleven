# Standard libraryy

# 3rd Party library
import pytest

# Project library


#----------------------------------------------------
@pytest.mark.parametrize(
    "number, expected",
    [
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
        (6,6),
        (7,"Seven"),
        (8,8),
        (9,9),
        (10,10),
        (11,"Eleven"),
        (14,"Seven"),
        (21,"Seven"),
        (22,"Eleven"),
        (77,"7-Eleven"),
        (78,78),
        (154,"7-Eleven")
    ]
)
def test_print_7_eleven(number,expected):
    """Print 7-eleven"""
    # Arrange
    # Act
    # Assert
