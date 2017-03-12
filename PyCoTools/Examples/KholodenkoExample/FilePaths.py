# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 10:40:12 2017

@author: b3053674
"""
import os
import sys
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
 

Change the 'self.current_directory' string variable below to the directory containing 
your own KholodenkoExample folder. The if statement is there to enable use
of the same script on both linux and windows machines without modification
(i.e. for use with a linux based SGE cluster). If you do not have this facility 
available, just ignore it. 

 
'''

class KholodenkoExample():
    def __init__(self):
        ## path to folder containing kholodenko example
        if sys.platform=='win32':
            self.current_directory='D:\MPhil\Python\My_Python_Modules\Modelling_Tools\PyCoTools\PyCoTools\Examples\KholodenkoExample'
        else:
            self.current_directory=r'/sharedlustre/users/b3053674/2017/Jan/Kholod/KholodenkoExample'
        
        ## Kholodenko filename
        self.copasi_filename=r'Kholodenko.cps'
        ## full path to kholodenko model
        self.kholodenko_model=os.path.join(self.current_directory,self.copasi_filename)
        ## full path to the time course output
        self.timecourse_report=os.path.join(self.current_directory,'KholodenkoTimeCourseOutput.txt')
        ## full path to the noisy time course output
        self.noisy_timecourse_report=os.path.join(self.current_directory,'NoisyKholodenkoTimeCourseOutput.txt')
        ## Full path to parameter estimation results file
        self.PEData_file=os.path.join(self.current_directory,'PEResultsFile.txt')
        ## Full path to a folder containing all data from initial multiple global parameter estimations
        self.PEData_dir=os.path.join(self.current_directory,'PEResults')
        ## Full path to file containing secondary local parameter estimation (starting with best values from self.PEData_dir)
#        self.local_PEData_file=os.path.join(self.current_directory,'LocalPEData.txt')
        self.local_PEData_dir=os.path.join(self.current_directory,'LocalPEDataResults')
        ## path to PEData Pickle
        
        self.PE_data_global1=os.path.join(self.current_directory,'1GlobalPEData.pickle')
        self.PE_data_local1=os.path.join(self.current_directory,'1LocalPEData.pickle')

        self.PE_data_global2=os.path.join(self.current_directory,'2GlobalPEData.pickle')
        self.PE_data_local2=os.path.join(self.current_directory,'2LocalPEData.pickle')
        












