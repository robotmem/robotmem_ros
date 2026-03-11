# Copyright 2026 gladego
#
# Licensed under the MIT License.

from ament_pep257.main import main
import pytest


@pytest.mark.linter
@pytest.mark.pep257
def test_pep257():
    """Check docstring conventions with pep257."""
    rc = main(argv=['.', 'test'])
    assert rc == 0, 'Found code style errors / warnings'
