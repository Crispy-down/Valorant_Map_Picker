# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=['C:\\Users\\brian\\OneDrive\\바탕 화면\\CODE\\val_project'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

a.datas += [('val.png', './val.png', "DATA")]
a.datas += [('bg_3.png', './bg_3.png', "DATA")]
a.datas += [('ATK_bg.png', './ATK_bg.png', "DATA")]
a.datas += [('DEF_bg.png', './DEF_bg.png', "DATA")]
a.datas += [('unknown.png', './unknown.png', "DATA")]

a.datas += [('Red_team.png', './Red_team.png', "DATA")]
a.datas += [('Blue_team.png', './Blue_team.png', "DATA")]
a.datas += [('haven_set.png', './haven_set.png', "DATA")]
a.datas += [('fracture_set.png', './fracture_set.png', "DATA")]
a.datas += [('split_set.png', './split_set.png', "DATA")]

a.datas += [('icebox_set.png', './icebox_set.png', "DATA")]
a.datas += [('pearl_set.png', './pearl_set.png', "DATA")]
a.datas += [('ascent_set.png', './ascent_set.png', "DATA")]
a.datas += [('lotus_set.png', './lotus_set.png', "DATA")]
a.datas += [('Ascent_normal.png', './Ascent_normal.png', "DATA")]

a.datas += [('Fracture_normal.png', './Fracture_normal.png', "DATA")]
a.datas += [('Split_normal.png', './Split_normal.png', "DATA")]
a.datas += [('Lotus_normal.png', './Lotus_normal.png', "DATA")]
a.datas += [('Pearl_normal.png', './Pearl_normal.png', "DATA")]
a.datas += [('Icebox_normal.png', './Icebox_normal.png', "DATA")]

a.datas += [('Haven_normal.png', './Haven_normal.png', "DATA")]
a.datas += [('Ascent_pick.png', './Ascent_pick.png', "DATA")]
a.datas += [('Fracture_pick.png', './Fracture_pick.png', "DATA")]
a.datas += [('Split_pick.png', './Split_pick.png', "DATA")]
a.datas += [('Lotus_pick.png', './Lotus_pick.png', "DATA")]

a.datas += [('Pearl_pick.png', './Pearl_pick.png', "DATA")]
a.datas += [('Icebox_pick.png', './Icebox_pick.png', "DATA")]
a.datas += [('Haven_pick.png', './Haven_pick.png', "DATA")]
a.datas += [('Ascent_ban.png', './Ascent_ban.png', "DATA")]
a.datas += [('Fracture_ban.png', './Fracture_ban.png', "DATA")]

a.datas += [('Split_ban.png', './Split_ban.png', "DATA")]
a.datas += [('Lotus_ban.png', './Lotus_ban.png', "DATA")]
a.datas += [('Pearl_ban.png', './Pearl_ban.png', "DATA")]
a.datas += [('Icebox_ban.png', './Icebox_ban.png', "DATA")]
a.datas += [('Haven_ban.png', './Haven_ban.png', "DATA")]



pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Valorant_Map_Selector',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['val.ico'],
)
