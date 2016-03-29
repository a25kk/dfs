# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from dfs.buildout.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of dfs.buildout into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if dfs.buildout is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('dfs.buildout'))

    def test_uninstall(self):
        """Test if dfs.buildout is cleanly uninstalled."""
        self.installer.uninstallProducts(['dfs.buildout'])
        self.assertFalse(self.installer.isProductInstalled('dfs.buildout'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IDfsBuildoutLayer is registered."""
        from dfs.buildout.interfaces import IDfsBuildoutLayer
        from plone.browserlayer import utils
        self.failUnless(IDfsBuildoutLayer in utils.registered_layers())
