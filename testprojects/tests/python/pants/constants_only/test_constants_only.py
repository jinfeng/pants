# coding=utf-8
# Copyright 2014 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import (nested_scopes, generators, division, absolute_import, with_statement,
                        print_function, unicode_literals)


def test_constants_only():
  try:
    from pants.constants_only.constants import VALID_IDENTIFIERS
  except ImportError as e:
    assert False, 'Failed to correctly generate python package: %s' % e
