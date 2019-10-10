import os


def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes


def infotodict(seqinfo):
    """Heuristic evaluator for determining which runs belong where

    allowed template fields - follow python string module:

    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group
    """

    t1w = create_key('sub-{subject}/anat/sub-{subject}_T1w')
    run1 = create_key('sub-{subject}/func/sub-{subject}_task-InstrAct_run-1_bold')
    run2 = create_key('sub-{subject}/func/sub-{subject}_task-InstrAct_run-2_bold')
    run3 = create_key('sub-{subject}/func/sub-{subject}_task-InstrAct_run-3_bold')
    run4 = create_key('sub-{subject}/func/sub-{subject}_task-InstrAct_run-4_bold')
    locdecl = create_key('sub-{subject}/func/sub-{subject}_task-locdecl_run-1_bold')
    locproc = create_key('sub-{subject}/func/sub-{subject}_task-locproc_run-1_bold')
    fm1 = create_key('sub-{subject}/fmap/sub-{subject}_magnitude')
    fm2 = create_key('sub-{subject}/fmap/sub-{subject}_phasediff')
    info = {t1w: [],
            run1: [],
            run2: [],
            run3: [],
            run4: [],
            locdecl: [],
            locproc: [],
            fm1: [],
            fm2: [],
            }

    for s in seqinfo:
        """
        The namedtuple `s` contains the following fields:

        * total_files_till_now
        * example_dcm_file
        * series_id
        * dcm_dir_name
        * unspecified2
        * unspecified3
        * dim1
        * dim2
        * dim3
        * dim4
        * TR
        * TE
        * protocol_name
        * is_motion_corrected
        * is_derived
        * patient_id
        * study_description
        * referring_physician_name
        * series_description
        * image_type
        """

        if s.protocol_name == 'GIfMI_T1_MPRAGE':
            info[t1w].append(s.series_id)
        if s.protocol_name == 'ep2d_bold_RUN_1':
            info[run1].append(s.series_id)
        if s.protocol_name == 'ep2d_bold_RUN_2':
            info[run2].append(s.series_id)
        if s.protocol_name == 'ep2d_bold_RUN_3':
            info[run3].append(s.series_id)
        if s.protocol_name == 'ep2d_bold_RUN_4':
            info[run4].append(s.series_id)
        if s.protocol_name == 'ep2d_bold_LOC_DECL':
            info[locdecl].append(s.series_id)
        if s.protocol_name == 'ep2d_bold_LOC_PROC':
            info[locproc].append(s.series_id)
        if s.protocol_name == 'gre_field_mapping_2.5mm' and s.dcm_dir_name =='GRE_FIELD_MAPPING_2_5MM_0006': #4 for subject 1
            info[fm1].append(s.series_id)
        if s.protocol_name == 'gre_field_mapping_2.5mm' and s.dcm_dir_name =='GRE_FIELD_MAPPING_2_5MM_0007': #5 for subject 1
            info[fm2].append(s.series_id)
    return info
