r"""
Features for testing the presence of ``sphinx``
"""

# *****************************************************************************
#       Copyright (C) 2021 Matthias Koeppe
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  https://www.gnu.org/licenses/
# *****************************************************************************

from . import PythonModule


class Sphinx(PythonModule):
    r"""
    A :class:`sage.features.Feature` describing the presence of :ref:`Sphinx <spkg_sphinx>`.

    Sphinx is provided by a standard package in the Sage distribution,
    but it can be disabled by ``configure --disable-doc``.

    EXAMPLES::

        sage: from sage.features.sphinx import Sphinx
        sage: Sphinx().is_present()                     # optional - sphinx
        FeatureTestResult('sphinx', True)
    """
    def __init__(self):
        r"""
        TESTS::

            sage: from sage.features.sphinx import Sphinx
            sage: isinstance(Sphinx(), Sphinx)
            True
        """
        PythonModule.__init__(self, 'sphinx', spkg='sphinx')


def all_features():
    return [Sphinx()]
