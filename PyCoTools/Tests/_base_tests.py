#-*-coding: utf-8 -*-
"""

 This file is part of PyCoTools.

 PyCoTools is free software: you can redistribute it and/or modify
 it under the terms of the GNU Lesser General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 PyCoTools is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU Lesser General Public License for more details.

 You should have received a copy of the GNU Lesser General Public License
 along with PyCoTools.  If not, see <http://www.gnu.org/licenses/>.


 $Author: Ciaran Welsh

Module that tests the operations of the _Base base test

"""

import site
site.addsitedir('C:\Users\Ciaran\Documents\PyCoTools')
import PyCoTools
from PyCoTools.Tests import _test_base
import os, glob
import pandas
import unittest
from lxml import etree




class TestBase(_test_base._BaseTest):
    def setUp(self):
        super(TestBase, self).setUp()
        self._base = PyCoTools._base._Base(A='a', B='b')

    def test_num_kwargs(self):
        ## 4 kwargs defined. A and B in setUp
        ## and the kwargs dict
        self.assertEqual(len(self._base.__dict__), 3)

    def test_set_random_attribute(self):
        self.assertEqual(self._base.A, 'a')

    def test_set_random_attribute2(self):
        self.assertEqual(self._base.B, 'b')

    def test_name(self):
        """
        Test that assignments work in a subclass
        :return:
        """
        print PyCoTools.model
        # comp = PyCoTools.model.Compartment(name='A', size=5)
        # self.assertTrue(comp.name=='A')
        # self.assertRaises(PyCoTools.pycopi.Compartment(not_a_key='raise exception'), PyCoTools.Errors.InputError)

    def test_setattr(self):
        self._base.A = 4
        self.assertEqual(self._base.A, 4)

    def test_str(self):
        kwarg_string = "A='a', B='b'"
        self.assertEqual(kwarg_string,self._base.as_string() )

    def test_as_df_index(self):
        index = ['A','B']
        self.assertListEqual(list(self._base.as_df().index ), index)

    def test_as_df_values(self):
        index = ['A','B']
        self.assertListEqual(list(self._base.as_df()['Value'] ), ['a','b'])

    def test_as_dict_values(self):
        keys = ['A', 'B']
        self.assertListEqual(keys, self._base.as_dict().keys())

    def test_as_dict_values(self):
        keys = ['a', 'b']
        self.assertListEqual(keys, self._base.as_dict().values())

#
class BaseModelTests(_test_base._BaseTest):
    def setUp(self):
        super(BaseModelTests, self).setUp()
        self._model_base_from_string = PyCoTools._base._ModelBase(self.copasi_file, A='a')
        self._model_base_from_element = PyCoTools._base._ModelBase(self._model_base_from_string.model, B='b')

    def test_from_path(self):
        """
        Test _ModelBase can get model from string to model
        path
        :return:
        """
        self.assertTrue(isinstance(self._model_base_from_string.model, etree._Element) )

    def test_from_etree(self):
        element_model = self._model_base_from_string.model
        self.assertTrue(isinstance(self._model_base_from_element.model, etree._Element))

    def test_kwargs(self):
        self.assertEqual(self._model_base_from_string.A, 'a')

    def test_as_string(self):
        self.assertTrue(isinstance(self._model_base_from_string.as_string(), str))

# class BaseModel2Tests(_test_base._BaseTest):
#     def setUp(self):
#         super(BaseModel2Tests, self).setUp()
#         self.model_base = PyCoTools._base._ModelBase(self.copasi_file)
# #
#     def test_test(self):
#         print self.model_base.model

if __name__ == '__main__':
    unittest.main()














