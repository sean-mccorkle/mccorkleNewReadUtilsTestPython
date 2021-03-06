# -*- coding: utf-8 -*-
#BEGIN_HEADER
# The header block is where all import statments should live
import sys
import traceback
import uuid
from pprint import pprint, pformat
from biokbase.workspace.client import Workspace as workspaceService
from ReadsUtils.ReadsUtilsClient import ReadsUtils
import os
import pprint
#END_HEADER


class mccorkleNewReadUtilsTestPython:
    '''
    Module Name:
    mccorkleNewReadUtilsTestPython

    Module Description:
    A KBase module: mccorkleNewReadUtilsTestPython
This sample module contains one small method - filter_contigs.
    '''

    ######## WARNING FOR GEVENT USERS #######
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    #########################################
    VERSION = "0.0.1"
    GIT_URL = "https://github.com/sean-mccorkle/mccorkleNewReadUtilsTestPython.git"
    GIT_COMMIT_HASH = "6a48ab1da38fe4ba186bb8306ff29c8a0542f192"
    
    #BEGIN_CLASS_HEADER
    # Class variables and functions can be defined in this block
    workspaceURL = None
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.workspaceURL = config['workspace-url']
        self.callbackURL = os.environ['SDK_CALLBACK_URL']
        #END_CONSTRUCTOR
        pass
    

    def filter_contigs(self, ctx, params):
        """
        Filter contigs in a ContigSet by DNA length
        :param params: instance of type "FilterContigsParams" -> structure:
           parameter "workspace" of type "workspace_name" (A string
           representing a workspace name.), parameter "contigset_id" of type
           "contigset_id" (A string representing a ContigSet id.), parameter
           "min_length" of Long
        :returns: instance of type "FilterContigsResults" -> structure:
           parameter "report_name" of String, parameter "report_ref" of
           String, parameter "new_contigset_ref" of type "ws_contigset_id"
           (The workspace ID for a ContigSet data object. @id ws
           KBaseGenomes.ContigSet), parameter "n_initial_contigs" of Long,
           parameter "n_contigs_removed" of Long, parameter
           "n_contigs_remaining" of Long
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN filter_contigs
        
        # Print statements to stdout/stderr are captured and available as the method log
        print('Starting filter contigs method.')
        

        # Step 1 - Parse/examine the parameters and catch any errors
        # It is important to check that parameters exist and are defined, and that nice error
        # messages are returned to the user
        if 'workspace' not in params:
            raise ValueError('Parameter workspace is not set in input arguments')
        workspace_name = params['workspace']
        if 'contigset_id' not in params:
            raise ValueError('Parameter contigset_id is not set in input arguments')
        contigset_id = params['contigset_id']
        if 'min_length' not in params:
            raise ValueError('Parameter min_length is not set in input arguments')
        min_length_orig = params['min_length']
        min_length = None
        try:
            min_length = int(min_length_orig)
        except ValueError:
            raise ValueError('Cannot parse integer from min_length parameter (' + str(min_length_orig) + ')')
        if min_length < 0:
            raise ValueError('min_length parameter shouldn\'t be negative (' + str(min_length) + ')')
        

        # Step 2- Download the input data
        # Most data will be based to your method by its workspace name.  Use the workspace to pull that data
        # (or in many cases, subsets of that data).  The user token is used to authenticate with the KBase
        # data stores and other services.  DO NOT PRINT OUT OR OTHERWISE SAVE USER TOKENS
        token = ctx['token']
        wsClient = workspaceService(self.workspaceURL, token=token) 
        try: 
            # Note that results from the workspace are returned in a list, and the actual data is saved
            # in the 'data' key.  So to get the ContigSet data, we get the first element of the list, and
            # look at the 'data' field.
            contigSet = wsClient.get_objects([{'ref': workspace_name+'/'+contigset_id}])[0]['data']
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            orig_error = ''.join('    ' + line for line in lines)
            raise ValueError('Error loading original ContigSet object from workspace:\n' + orig_error)
        
        print('Got ContigSet data.')
        

        # Step 3- Actually perform the filter operation, saving the good contigs to a new list
        good_contigs = []
        n_total = 0;
        n_remaining = 0;
        for contig in contigSet['contigs']:
            n_total += 1
            if len(contig['sequence']) >= min_length:
                good_contigs.append(contig)
                n_remaining += 1

        # replace the contigs in the contigSet object in local memory
        contigSet['contigs'] = good_contigs
        
        print('Filtered ContigSet to '+str(n_remaining)+' contigs out of '+str(n_total))
        

        # Step 4- Save the new ContigSet back to the Workspace
        # When objects are saved, it is important to always set the Provenance of that object.  The basic
        # provenance info is given to you as part of the context object.  You can add additional information
        # to the provenance as necessary.  Here we keep a pointer to the input data object.
        provenance = [{}]
        if 'provenance' in ctx:
            provenance = ctx['provenance']
        # add additional info to provenance here, in this case the input data object reference
        provenance[0]['input_ws_objects']=[workspace_name+'/'+contigset_id]

        obj_info_list = None
        try:
	        obj_info_list = wsClient.save_objects({
	                            'workspace':workspace_name,
	                            'objects': [
	                                {
	                                    'type':'KBaseGenomes.ContigSet',
	                                    'data':contigSet,
	                                    'name':contigset_id,
	                                    'provenance':provenance
	                                }
	                            ]
	                        })
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            orig_error = ''.join('    ' + line for line in lines)
            raise ValueError('Error saving filtered ContigSet object to workspace:\n' + orig_error)
        
        info = obj_info_list[0]
        # Workspace Object Info is a tuple defined as-
        # absolute ref = info[6] + '/' + info[0] + '/' + info[4]
        # 0 - obj_id objid - integer valued ID of the object
        # 1 - obj_name name - the name of the data object
        # 2 - type_string type - the full type of the data object as: [ModuleName].[Type]-v[major_ver].[minor_ver]
        # 3 - timestamp save_date
        # 4 - int version - the object version number
        # 5 - username saved_by
        # 6 - ws_id wsid - the unique integer valued ID of the workspace containing this object
        # 7 - ws_name workspace - the workspace name
        # 8 - string chsum - md5 of the sorted json content
        # 9 - int size - size of the json content
        # 10 - usermeta meta - dictionary of string keys/values of user set or auto generated metadata

        print('saved ContigSet:'+pformat(info))


        # Step 5- Create the Report for this method, and return the results
        # Create a Report of the method
        report = 'New ContigSet saved to: '+str(info[7]) + '/'+str(info[1])+'/'+str(info[4])+'\n'
        report += 'Number of initial contigs:      '+ str(n_total) + '\n'
        report += 'Number of contigs removed:      '+ str(n_total - n_remaining) + '\n'
        report += 'Number of contigs in final set: '+ str(n_remaining) + '\n'

        reportObj = {
            'objects_created':[{
                    'ref':str(info[6]) + '/'+str(info[0])+'/'+str(info[4]), 
                    'description':'Filtered Contigs'
                }],
            'text_message':report
        }

        # generate a unique name for the Method report
        reportName = 'filter_contigs_report_'+str(hex(uuid.getnode()))
        report_info_list = None
        try:
            report_info_list = wsClient.save_objects({
                    'id':info[6],
                    'objects':[
                        {
                            'type':'KBaseReport.Report',
                            'data':reportObj,
                            'name':reportName,
                            'meta':{},
                            'hidden':1, # important!  make sure the report is hidden
                            'provenance':provenance
                        }
                    ]
                })
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            orig_error = ''.join('    ' + line for line in lines)
            raise ValueError('Error saving filtered ContigSet object to workspace:\n' + orig_error)
        
        report_info = report_info_list[0]

        print('saved Report: '+pformat(report_info))

        returnVal = {
                'report_name': reportName,
                'report_ref': str(report_info[6]) + '/' + str(report_info[0]) + '/' + str(report_info[4]),
                'new_contigset_ref': str(info[6]) + '/'+str(info[0])+'/'+str(info[4]),
                'n_initial_contigs':n_total,
                'n_contigs_removed':n_total-n_remaining,
                'n_contigs_remaining':n_remaining
            }
        
        print('returning:'+pformat(returnVal))
                
        #END filter_contigs

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method filter_contigs return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def upload_fastq(self, ctx, params):
        """
        :param params: instance of type "UploadFastqParams" (testing
           invocation of ReadsUtils) -> structure: parameter "fwd_id" of
           String, parameter "wsid" of Long, parameter "wsname" of String,
           parameter "objid" of Long, parameter "name" of String, parameter
           "rev_id" of String, parameter "sequencing_tech" of String
        :returns: instance of type "UploadFastqObjref"
        """
        # ctx is the context object
        # return variables are: objref
        #BEGIN upload_fastq
        print( "hai this is upload_fastq here, params are")
        pprint.pprint( params )
        ReadsUtils_instance = ReadsUtils(url=self.callbackURL, token=ctx['token'], service_ver='dev')
        print( "got ReadsUtilsinstance")
        method_retVal = ReadsUtils_instance.upload_reads( params )
        print( "back from ReadsUtils_instance.upload_reads")
        pprint( method_retVal )
        objref = "Vooch"
        #END upload_fastq

        # At some point might do deeper type checking...
        if not isinstance(objref, basestring):
            raise ValueError('Method upload_fastq return value ' +
                             'objref is not type basestring as required.')
        # return the results
        return [objref]

    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK", 'message': "", 'version': self.VERSION, 
                     'git_url': self.GIT_URL, 'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
