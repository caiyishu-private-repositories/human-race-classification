@echo off
if not exist "snapshots\" md "snapshots"
rem C:\caffe\caffe.exe train -solver solver_dpe_220_v4.prototxt -log_dir=snapshots
rem C:\caffe\caffe.exe train -solver solver_dpe_220_v4.prototxt -weights snapshots\_iter_40000.caffemodel -log_dir=snapshots
C:\caffe\caffe.exe test -model train_val_dpe_220_v4.prototxt -weights snapshots\_iter_40000.caffemodel -gpu 0 -iterations 100 -log_dir=snapshots
pause