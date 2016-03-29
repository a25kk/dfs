# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from dfs.sitecontent.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of dfs.sitecontent into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if dfs.sitecontent is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('dfs.sitecontent'))

    def test_uninstall(self):
        """Test if dfs.sitecontent is cleanly uninstalled."""
        self.installer.uninstallProducts(['dfs.sitecontent'])
        self.assertFalse(self.installer.isProductInstalled('dfs.sitecontent'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IDfsSitecontentLayer is registered."""
        from dfs.sitecontent.interfaces import IDfsSitecontentLayer
        from plone.browserlayer import utils
        self.failUnless(IDfsSitecontentLayer in utils.registered_layers())
