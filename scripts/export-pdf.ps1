$ErrorActionPreference = "Stop"
$PythonExe = Join-Path $PSScriptRoot "..\.venv\Scripts\python.exe"

if (-not (Test-Path $PythonExe)) {
    $PythonExe = "python"
}

Write-Host "Generating PDF bundle ..."
& $PythonExe ./scripts/generate_pdf_bundle.py

Write-Host "Building standalone PDF HTML ..."
& $PythonExe ./scripts/build_pdf_html.py
if ($LASTEXITCODE -ne 0) {
    throw "PDF HTML build failed."
}

Write-Host "Rendering PDF with Chromium ..."
try {
    & $PythonExe ./scripts/render_pdf.py --site-dir site --page pdf/handbook.html --output site/pdf/student-it-handbook.pdf

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
