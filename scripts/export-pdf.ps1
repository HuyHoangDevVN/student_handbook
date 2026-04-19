param(
    [string]$ConfigFile = "mkdocs-pdf.yml"
)

$ErrorActionPreference = "Stop"
$PythonExe = Join-Path $PSScriptRoot "..\.venv\Scripts\python.exe"

if (-not (Test-Path $PythonExe)) {
    $PythonExe = "python"
}

if (-not (Test-Path $ConfigFile)) {
    throw "Khong tim thay file cau hinh PDF: $ConfigFile"
}

Write-Host "Generating PDF bundle ..."
& $PythonExe ./scripts/generate_pdf_bundle.py

Write-Host "Building PDF site with config $ConfigFile ..."
& $PythonExe -m mkdocs build -f $ConfigFile
if ($LASTEXITCODE -ne 0) {
    throw "PDF site build failed."
}

Write-Host "Rendering PDF with Chromium ..."
try {
    & $PythonExe ./scripts/render_pdf.py --site-dir site --page _generated/handbook-pdf/ --output site/pdf/student-it-handbook.pdf

    if ($LASTEXITCODE -ne 0) {
        throw "PDF render failed."
    }
}
catch {
    Write-Host ""
    Write-Host "PDF build failed."
    Write-Host "Likely causes:"
    Write-Host "  - Playwright is not installed in the Python environment"
    Write-Host "  - Chromium browser for Playwright has not been installed yet"
    Write-Host "Recommended fixes:"
    Write-Host "  1. pip install -r requirements.txt"
    Write-Host "  2. python -m playwright install chromium"
    Write-Host "  3. rerun ./scripts/export-pdf.ps1"
    throw
}

Write-Host "PDF build completed. Check site/pdf/student-it-handbook.pdf"
