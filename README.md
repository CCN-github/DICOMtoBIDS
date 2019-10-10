# DICOMtoBIDS
How to use HeuDiConv (Heuristic DICOM Converter) to transform raw DICOM data into a BIDS dataset

# Documentation and tutorials
https://github.com/nipy/heudiconv
http://nipy.org/heudiconv/#10
https://www.youtube.com/watch?v=O1kZAuR7E00

*This how-to is adapted to use with docker (http://docker.com)

# FIRST STEP: Create heuristic file (see convertKeys.py)

Copy the following code and paste it in a terminal:

docker run --rm -it \
-v ~/../../../d/UGentData/fMRI/dicom:/data:ro \
-v ~/../../../d/UGentData/fMRI/BIDS:/output \
nipy/heudiconv:latest \
-d /data/{subject}/*/*/*.IMA \
-s '01' \
-f convertall \
-c none \
-o /output

This will create a .heudiconv folder with a file called "convertall.py". You will have to adapt this file to the specifics of your study (see convert_retro.py file for an example).

At this point, move your new heuristic file to your script folder and delete the .heudiconv folder

# Run the transformation with our heuristic file
for subject in {01..05}; do
	docker run --rm -it \
	-v ~/../../../d/UGentData/fMRI/dicom:/data:ro \
	-v ~/../../../d/UGentData/fMRI/BIDS:/output \
	nipy/heudiconv:latest \
	-d /data/{subject}/*/*/*.IMA \
	-s ${subject} \
	-f /data/scripts/convert_retro.py \
	-c dcm2niix -b \
	-o /output \
	--minmeta
done
