# DICOMtoBIDS
How to use HeuDiConv (Heuristic DICOM Converter) to transform raw DICOM data into a BIDS dataset

#documentation and tutorials
# https://github.com/nipy/heudiconv
# http://nipy.org/heudiconv/#10
# https://www.youtube.com/watch?v=O1kZAuR7E00

*This how-to is adapted to use with docker (http://docker.com)

#FIRST STEP: Create heuristic file (see convertKeys.py)

# ONLY after having created our heuristic file, use dcm2niix to transform
# the dicom files to nifti, using BIDS formatting.
# Copy the following code and paste it in a terminal:

docker run --rm -it \
-v ~/../../../d/UGentData/fMRI/dicom:/data:ro \
-v ~/../../../d/UGentData/fMRI/BIDS:/output \
nipy/heudiconv:latest \
-d /data/{subject}/*/*/*.IMA \
-s '01' \
-f convertall \
-c none \
-o /output

At this point, delent the .heudiconv file
# Run the transformation with our heuristic file
for subject in {01..05}; do
	docker run --rm -it \
	-v ~/../../../d/UGentData/fMRI/dicom:/data:ro \
	-v ~/../../../d/UGentData/fMRI/BIDS:/output \
	nipy/heudiconv:latest \
	-d /data/{subject}/*/*/*.IMA \
	-s ${subject} \
	-f /data/scripts/convert_heuristic.py \
	-c dcm2niix -b \
	-o /output \
	--minmeta
done
