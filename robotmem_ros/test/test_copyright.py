# Copyright 2026 gladego
#
# Licensed under the MIT License.

from ament_copyright.main import main
import pytest


@pytest.mark.copyright
@pytest.mark.linter
def test_copyright():
    """Check all files have copyright notice."""
    rc = main(argv=['.', 'test'])
    assert rc == 0, 'Found errors'
