Google CameraTrap AI: How- To
Prepared by Lukas Kopacki, ArborVox


NOTE: Please see attached word document for helpful screenshots and context.

I.	 Resources
Project GitHub: google/cameratrapai: AI models trained by Google to classify species in images from motion-triggered widlife cameras.
Post-Processing Script Github: lkopacki/CameraTrapAI_PostProcess: A script to produce a picture-by-picture species prediction summary, as well as species-based sorting functions.
Optional Resources:
Anaconda Download: Download Anaconda Distribution | Anaconda
Python Download: Download Python | Python.org

II.	Set-up and Running of the Model
1.	Follow the steps in the ‘Installing Python’ page, including installing Miniforge.
2.	Once the environment is set up, navigate back to the main page of the Github, and follow the directions as specified in ‘Running SpeciesNet’.
a.	Running the models (Example)
python -m speciesnet.scripts.run_model --folders "[copy path to folder where photos are] " copy folder path where you want the report to be placed] " --admin1_region [2-letter state abbreviation]
For example, my code while running photos taken in Washington state looked like this:
python -m speciesnet.scripts.run_model --folders "C:\Users\LukasKopacki\Downloads\RP24.2 C4 Cam2 RAW-20250318T010058Z-001" --predictions_json "C:\Users\LukasKopacki\Downloads\OutputsForCCP\RP24.2 C4 Cam2 RAW-20250318T010058Z-001.json" --admin1_region WA
3.	Once you have entered the string as needed, press enter. The model should run for quite some time. The shell should look like the example below once complete:
 
III.	Post-Processing: Summary File and Photo Sorting
1.	Navigate to the Post Processing Github and download the python file. 
 
2.	Open ‘IDLE (Python)….’ On your computer and open the file. It should look like below:
  
3.	Input the desired paths, and click run. 
a.	You may need to install packages if you have not run python before. This requires you to type in the kernel (see below) ‘pip install [package]’
 
4.	Check the specified path for the final data outputs.

