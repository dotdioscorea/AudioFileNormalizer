import soundfile as sf
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os
import sys
import numpy as np
import shutil
from PIL import Image, ImageTk

# Function to normalize the volume of an audio file using soundfile
def normalize_volume(filepath, target_dBFS):
    # Load the audio file using soundfile
    data, sample_rate = sf.read(filepath)

    # Calculate the current RMS level of the audio signal
    rms = data.std()

    # Calculate the target RMS level, which is the RMS level that
    # corresponds to the target dBFS level
    target_rms = 10**((target_dBFS - 20 * np.log10(rms))/20)

    # Scale the audio signal so that its RMS level matches the target RMS level
    data = data * target_rms

    # Write the normalized audio signal back to the original file
    sf.write(filepath, data, sample_rate)

# Function to update the status label
def update_status(status):
    status_label.config(text=status)

# Function to browse for a directory
def browse():
    dirpath = filedialog.askdirectory()
    if dirpath:
        dirpath_entry.delete(0, tk.END)
        dirpath_entry.insert(0, dirpath)

# Function to browse for an output directory
def browse_outdir():
    dirpath = filedialog.askdirectory()
    if dirpath:
        outdir_entry.delete(0, tk.END)
        outdir_entry.insert(0, dirpath)

# Function to normalize the volume of all audio files in a directory
def normalize():
    # Get the target volume level from the volume slider
    target_dBFS = volume_slider.get()

    # Get the path of the input and output directories
    dirpath = dirpath_entry.get()
    outdir = outdir_entry.get()

    # List all audio files in the directory
    try:
        audio_files = [f for f in os.listdir(dirpath) if f.endswith('.mp3')]
    except Exception as e:
        # Update the status label with the error message
        update_status(f'Error processing: {str(e)}')

    # Update the status label
    update_status('Normalizing audio files... (1/' + str(len(audio_files)) + ')')

    # Process the audio files one by one
    for i, file in enumerate(audio_files):
        # Update the progress bar
        progress_bar.config(value=(i+1)/len(audio_files))

        # Copy the audio file to the output directory

        try:
            filepath = os.path.join(dirpath, file)
            filename, ext = os.path.splitext(file)
            outfile = filename + '_normalized' + ext
            outfilepath = os.path.join(outdir, outfile)
            shutil.copyfile(filepath, outfilepath)
        except Exception as e:
            # Update the status label with the error message
            update_status(f'Error processing {filename}: {str(e)}')

        # Normalize the volume of the copied file
        normalize_volume(outfilepath, target_dBFS)

        update_status('Normalizing audio files... (' + str(i+1) + '/' + str(len(audio_files)) + ')')

    # Update the status label
    update_status('Finished normalizing audio files.')

    # Get the target volume level from the volume slider
    target_dBFS = volume_slider.get()

    # Get the path of the input and output directories
    dirpath = dirpath_entry.get()
    outdir = outdir_entry.get()

    # List all audio files in the directory
    audio_files = [f for f in os.listdir(dirpath) if f.endswith('.mp3')]

    # Update the status label
    update_status('Normalizing audio files... (1/' + str(audio_files.count))

    # Process the audio files one by one
    for i, file in enumerate(audio_files):
        # Update the progress bar
        progress_bar.config(value=(i+1)/len(audio_files))

        # Copy the audio file to the output directory
        filepath = os.path.join(dirpath, file)
        filename, ext = os.path.splitext(file)
        outfile = filename + '_normalized' + ext
        outfilepath = os.path.join(outdir, outfile)
        shutil.copyfile(filepath, outfilepath)

        # Normalize the volume of the copied file
        normalize_volume(outfilepath, target_dBFS)

        update_status('Normalizing audio files... (' + str(i) + '/' + str(audio_files.count))

    # Update the status label
    update_status('Finished normalizing audio files.')

# Create the main window
root = tk.Tk()
root.title('Audio Normalizer')

# Create the main container
mainframe = ttk.Frame(root, padding='5 5 5 5')
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

# Create the widgets
dirpath_label = ttk.Label(mainframe, text='Directory path:')
dirpath_entry = ttk.Entry(mainframe)
browse_button = ttk.Button(mainframe, text='Browse', command=browse)
outdir_label = ttk.Label(mainframe, text='Output directory:')
outdir_entry = ttk.Entry(mainframe)
outdir_browse_button = ttk.Button(mainframe, text='Browse', command=browse_outdir)

# Place the widgets in the main window
outdir_label.grid(column=1, row=3, sticky=tk.W)
outdir_entry.grid(column=2, row=3, sticky=(tk.W, tk.E))
outdir_browse_button.grid(column=3, row=3, sticky=tk.E)
volume_label = ttk.Label(mainframe, text='Volume level:')
volume_slider = tk.Scale(mainframe, from_=-20, to=10, orient=tk.HORIZONTAL)
volume_value_label = ttk.Label(mainframe, text='')
normalize_button = ttk.Button(mainframe, text='Normalize', command=normalize)
status_label = ttk.Label(mainframe, text='Awaiting user input', font=('Helvetica', 10))
progress_bar = ttk.Progressbar(mainframe, mode='determinate')

# Load the image file
try:
   wd = sys._MEIPASS
except AttributeError:
   wd = os.getcwd()
imagepath = os.path.join(wd,'logo.png')
img = Image.open(imagepath)
img = img.resize((50, 50))
img_tk = ImageTk.PhotoImage(img)
img_label = ttk.Label(mainframe, image=img_tk)
title_label = ttk.Label(mainframe, text='Audio Normalizer - dotdioscorea 2022', font=('Helvetica', 10))

# Place the widgets in the main window
dirpath_label.grid(column=1, row=1, sticky=tk.E)
dirpath_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))
browse_button.grid(column=3, row=1, sticky=tk.E)
outdir_label.grid(column=1, row=2, sticky=tk.E)
outdir_entry.grid(column=2, row=2, sticky=(tk.W, tk.E))
outdir_browse_button.grid(column=3, row=2, sticky=tk.E)
volume_label.grid(column=1, row=3, sticky=(tk.E, tk.S))
volume_slider.grid(column=2, row=3, sticky=(tk.W, tk.E))
volume_value_label.grid(column=3, row=3, sticky=tk.E)
normalize_button.grid(column=2, row=4, sticky=tk.E)
status_label.grid(column=1, row=5, columnspan=3, sticky=(tk.W, tk.E))
progress_bar.grid(column=1, row=6, columnspan=3, sticky=(tk.W, tk.E))
title_label.grid(column=1, row=7, columnspan=2, sticky=(tk.W, tk.E))
img_label.grid(column=3, row=3, rowspan=2)

#Make the widgets stretch with the window
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(2, weight=1)

#Bind the volume_value_label to the volume_slider
def update_volume_value_label(event):
    volume_value_label.config(text=str(volume_slider.get()))
    volume_slider.bind('<ButtonRelease>', update_volume_value_label)

#Run the main event loop
root.mainloop()
