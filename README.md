# Audio Normalizer
This script normalizes the volume of all audio files in a specified directory using the Python library soundfile.

## Requirements
Python 3
soundfile
numpy
tkinter
pillow
Usage
To use the script, run it in your Python environment, then follow the instructions on the GUI. You can specify the directory containing the audio files you want to normalize and the output directory where the normalized files will be saved. You can also adjust the target volume level using the volume slider.

## Usage

```python3 audio_normalizer.py```

## Functionality
The script has the following functions:

-normalize_volume(): This function normalizes the volume of an audio file. It takes the filepath and the target dBFS level as arguments, and returns nothing.

-update_status(): This function updates the status label on the GUI with the specified status message. It takes the status message as an argument and returns nothing.

-browse(): This function opens a file browser and allows the user to select a directory. It takes no arguments and returns nothing.

-browse_outdir(): This function is similar to browse(), but it allows the user to select the output directory where the normalized audio files will be saved.

normalize(): This function normalizes the volume of all audio files in the specified directory. It takes no arguments and returns nothing.

## GUI
The script uses the tkinter library to create a simple GUI that allows the user to interact with the script. The GUI has the following elements:

-A text entry field for specifying the input directory containing the audio files to be normalized.
-A browse button for opening a file browser and selecting the input directory.
-A text entry field for specifying the output directory where the normalized audio files will be saved.
-A browse button for opening a file browser and selecting the output directory.
-A volume slider for adjusting the target volume level.
-A normalize button for starting the normalization process.
-A status label for displaying the current status of the script.
-A progress bar for showing the progress of the normalization process.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
