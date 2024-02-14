# ecg2plot
Small python program that export dicom waveform into ecg plot. Runs in batchmode.
Also it creates an metadata output, with the plot uniqe filename and the dicom origin, so that the plot output is anonymouse from the dicom source data.
But can be back tracked via the metadata output.

Requires pydicom and matplotlib

Usage:
#   ..\Programs\Python\Python310>python ..\ecg2plt.py --x <..\Dicom path>
For batch mode operation:
#   FOR /F %G IN (ecg_joblist.txt) DO ..\PYTHON.EXE ..\ecg2plt.py --x %G
where the ecg_joblist.txt is an list of all dicom file to prosess. Use fully qualified path.

@Erland Ronningen
