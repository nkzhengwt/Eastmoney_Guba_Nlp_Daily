matlab -wait -nodesktop -nosplash -nodisplay -r "cd('%cd%');code_txt();quit"
py guba_daily.py
matlab -wait -nodesktop -nosplash -nodisplay -r "cd('%cd%');save_guba();quit"
pause