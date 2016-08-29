/*
A KBase module: mccorkleNewReadUtilsTestPython
This sample module contains one small method - filter_contigs.
*/

module mccorkleNewReadUtilsTestPython {
    /*
        A string representing a ContigSet id.
    */
    typedef string contigset_id;

    /*
        A string representing a workspace name.
    */
    typedef string workspace_name;

    typedef structure {
        workspace_name workspace;
        contigset_id contigset_id;
        int min_length;
    } FilterContigsParams;

    /* 
        The workspace ID for a ContigSet data object.
        @id ws KBaseGenomes.ContigSet
    */
    typedef string ws_contigset_id;

    typedef structure {
        string report_name;
        string report_ref;
        ws_contigset_id new_contigset_ref;
        int n_initial_contigs;
        int n_contigs_removed;
        int n_contigs_remaining;
    } FilterContigsResults;
	
    /*
        Filter contigs in a ContigSet by DNA length
    */
    funcdef filter_contigs(FilterContigsParams params) returns (FilterContigsResults) authentication required;

    /* testing invocation of ReadsUtils */

    typedef structure {
        string fwd_id;
        int wsid;
        string wsname;
        int objid;
        string name;
        string rev_id;
        string sequencing_tech;
        /* boolean single_genome; */
        /* KBaseCommon.StrainInfo strain; */
        /* KBaseCommon.SourceInfo source; */
        /* boolean interleaved; */
        /* boolean read_orientation_outward; */
        /* float insert_size_mean; */
        /* float insert_size_std_dev; */
    } UploadFastqParams;

   
    typedef string UploadFastqObjref;


    funcdef upload_fastq( UploadFastqParams params) returns( UploadFastqObjref objref ) authentication required;

};