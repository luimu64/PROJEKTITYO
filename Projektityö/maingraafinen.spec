# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['maingraafinen.py'],
             pathex=['C:\\Users\\luimu\\Documents\\GitHub\\PROJEKTITYO\\Projektityö'],
             binaries=[],
             datas=[ ("resurssit\\", "resurssit")],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
		  a.binaries,
          a.zipfiles,
          a.datas,
		  name="Epiccu_Geimu",
          strip=False,
          debug=False,
          upx=True,
          console=False, icon="icon.ico")
