# Copyright 2026 gladego
#
# Licensed under the MIT License.

"""Basic import test for robotmem_ros."""

import pytest


def test_import_robotmem_ros():
    """Verify robotmem_ros package is importable."""
    import robotmem_ros  # noqa: F401
    assert robotmem_ros is not None
