# -*- coding: utf-8 -*-
'''
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


Author: 
    Ciaran Welsh
Date:
    12/03/2017

 Object:
 
'''

import PyCoTools
import unittest
import glob
import os
import shutil 

import TestModels
import lxml.etree as etree

MODEL_STRING = TestModels.TestModels.get_model1()




class EvaluateOptimizationPerformanceTests(unittest.TestCase):
    def setUp(self):
        self.copasi_file = os.path.join(os.getcwd(), 'test_model.cps')
        self.copasiML = etree.fromstring(MODEL_STRING)
        PyCoTools.pycopi.CopasiMLParser.write_copasi_file(self.copasi_file, self.copasiML)

        ## make time course report name and make sure its available
        self.timecourse_report_name=os.path.join(os.getcwd(),'timecourse.txt')
        if os.path.isfile(self.timecourse_report_name):
            os.remove(self.timecourse_report_name)
        ## do time course
        self.TC=PyCoTools.pycopi.TimeCourse(self.copasi_file,StepSize=100,Plot='false',
                                               Intervals=50,End=5000,
                                               ReportName=self.timecourse_report_name)
        ## make PE report name available
        self.PE_report_name=os.path.join(os.path.dirname(self.copasi_file),'PEdata.txt')

        PyCoTools.pycopi.PruneCopasiHeaders(self.timecourse_report_name,replace='true')
        
        self.PE=PyCoTools.pycopi.ParameterEstimation(self.copasi_file,
                                                        self.timecourse_report_name,
                                                        PopulationSize=2,
                                                        NumberOfGenerations=2,
                                                        RandomizeStartValues='true',
                                                        ReportName=self.PE_report_name,
                                                        Plot='false')
        self.PE.write_item_template()
        self.PE.set_up()
        
        PyCoTools.pycopi.Scan(self.copasi_file,ScanType='repeat',NumberOfSteps=10,Run='true',
                                 ReportType='parameter_estimation',ReportName=self.PE_report_name)   
        
    def test_figure_is_produced(self):
        self.EOP= PyCoTools.PEAnalysis.EvaluateOptimizationPerformance(self.PE_report_name,
                                                                  Log10='true',
                                                                  SaveFig='true')
        self.assertEqual(len(os.listdir(self.EOP.results_dir)),1)
        
        
    def tearDown(self):
        os.remove(self.PE_report_name)
        for i in glob.glob('*.xlsx'):
            os.remove(i)
            
        for i in glob.glob('*.txt'):
            os.remove(i)
            
        for i in glob.glob('*.cps'):
            os.remove(i)    
            
        shutil.rmtree(self.EOP.results_dir)
        
        
    
    
    
if __name__=='__main__':
    unittest.main()
    