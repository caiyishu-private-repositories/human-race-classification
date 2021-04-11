@echo off
if not exist "snapshots\" md "snapshots"
C:\caffe\caffe.exe train -solver solver.prototxt -log_dir=snapshots
rem C:\caffe\caffe.exe train -solver solver_dpe_220_v4.prototxt -weights pretrained\_iter_8000.caffemodel -log_dir=snapshots
pause