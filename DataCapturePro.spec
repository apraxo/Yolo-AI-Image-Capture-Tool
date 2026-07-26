# -*- mode: python ; coding: utf-8 -*-
block_cipher = None
a = Analysis(['capture_app.py'],pathex=[],binaries=[],datas=[],
    hiddenimports=['pynput.mouse._win32','pynput.keyboard._win32',
        'pynput.mouse._darwin','pynput.keyboard._darwin',
        'pynput.mouse._xorg','pynput.keyboard._xorg',
        'onnxruntime','onnxruntime.capi','onnxruntime.capi.onnxruntime_inference_collection',
        'onnxruntime.capi._pybind_state','PIL._tkinter_finder','PIL.Image','PIL.ImageTk','PIL.ImageDraw',
        'mss','mss.windows','mss.darwin','mss.linux','cv2','numpy','tkinter','tkinter.ttk','tkinter.font',
        'tkinter.filedialog','tkinter.messagebox','ultralytics','ultralytics.models','ultralytics.engine',
        'torch','torchvision','queue',
        'cryptography','cryptography.hazmat.primitives.ciphers.aead',
        'cryptography.hazmat.bindings._rust','cffi','_cffi_backend'],
    hookspath=[],hooksconfig={},runtime_hooks=[],
    excludes=['matplotlib','scipy','pandas','IPython','jupyter'],
    win_no_prefer_redirects=False,win_private_assemblies=False,cipher=block_cipher,noarchive=False)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(pyz,a.scripts,[],exclude_binaries=True,name='DataCapturePro',debug=False,
    bootloader_ignore_signals=False,strip=False,upx=False,console=False,
    disable_windowed_traceback=False,argv_emulation=False,target_arch=None,
    codesign_identity=None,entitlements_file=None)
coll = COLLECT(exe,a.binaries,a.zipfiles,a.datas,strip=False,upx=False,upx_exclude=[],name='DataCapturePro')
