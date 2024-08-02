@echo off
setlocal enabledelayedexpansion

:: Caminho para o diretório raiz
set root_dir=.\deteccaoBorda

:: Arquivo de saída
set output_file=images_with_label_sim.txt

:: Limpar o arquivo de saída
if exist %output_file% del %output_file%

:: Comando ExifTool para verificar o rótulo
for /r "%root_dir%" %%f in (*.png) do (
    exiftool -s -s -Label -s "%%f" | findstr /i "Sim" >nul
    if !errorlevel! == 0 (
        echo %%f >> %output_file%
    )
)